#!/usr/bin/env python3
"""
Generate a video from a fixed image and an audio file (wav file), overlay 
the date of today on the image. The produced video 
has the image displayed throughout the entire duration of the audio. 
The output video is saved in the specified path.

Usage:
    python wav2vid.py path/to/image.jpg path/to/audio.wav path/to/output_video.mp4

Example:
    python wav2vid.py sample_image.jpg background_audio.wav output_video.mp4

Dependencies:
    - moviepy (Install with `pip install moviepy`)

"""
import os
import argparse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip


def add_date_to_image(image_path, output_image_path):
    """
    Adds today's date as text to the provided image.
    
    Args:
        image_path (str): Path to the original image file.
        output_image_path (str): Path to save the modified image with the date.
    """
    image = Image.open(image_path).convert("RGBA")
    draw = ImageDraw.Draw(image)

    # Get today's date
    today_date = datetime.now().strftime("%Y-%m-%d")
        
    # Scale font size based on image dimensions
    image_width, image_height = image.size
    # Font size is 5% of image width, minimum size is 20
    alpha = 0.1
    font_size = int(image_width * alpha)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default(font_size)

    # Calculate text position (top-left corner with padding)
    # Padding is 2% of image width, minimum is 10
    padding = max(10, int(image_width * 0.02))  
    text_position = (padding, padding) # Top-left corner
    
    # Add text to a transparent overlay
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.text(text_position, 
                      today_date, 
                      fill=(0, 0, 0, 255), 
                      font=font)
    
    # Composite the overlay onto the original image
    combined = Image.alpha_composite(image, overlay)

    # Check output format and convert if necessary
    if output_image_path.lower().endswith(".jpg") or \
        output_image_path.lower().endswith(".jpeg"):
        combined = combined.convert("RGB")  # Remove alpha channel for JPEG

    # Save the modified image
    combined.save(output_image_path)


def generate_video(image_path, audio_path, output_path):
    """
    Generates a video using a fixed image with today's date and an audio file.
    
    Args:
        image_path (str): Path to the image file (e.g., .jpg, .png).
        audio_path (str): Path to the audio file (.wav).
        output_path (str): Path where the output video file will be saved (e.g., .mp4).
    """
    # Load the image and audio
    image_clip = ImageClip(image_path)
    audio_clip = AudioFileClip(audio_path)
    
    # Set the duration of the image clip to match the audio clip
    image_clip = image_clip.set_duration(audio_clip.duration)
    
    # Set the audio for the image clip
    video = image_clip.set_audio(audio_clip)
    
    # Set the video format
    video = video.set_fps(24)  # Optional, set frames per second
    
    # Write the video to the output file
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')


def parse_arguments():
    """
    Parses command-line arguments for input image, audio, and output video paths.
    
    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate a video from a fixed image and an audio \
        file with today's date overlaid.")
    parser.add_argument("image_path", 
                        type=str, 
                        help="Path to the image file (e.g., .jpg, .png).")
    parser.add_argument("audio_path", 
                        type=str, 
                        help="Path to the audio file (.wav).")
    parser.add_argument("output_path", 
                        type=str, 
                        help="Path where the output video file \
                            will be saved (e.g., .mp4).")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    
    # Path for the modified image with the date
    modified_image_path = "modified_image.jpg"
    
    # Add date to the image
    add_date_to_image(args.image_path, modified_image_path)
    
    # Generate video using the modified image
    generate_video(modified_image_path, args.audio_path, args.output_path)

    # delete image
    os.remove(modified_image_path)