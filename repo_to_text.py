"""
repo_to_text.py

This script processes a local GitHub repository by concatenating the contents of its files into text files, with a specified word limit per file.

Usage:
    python repo_to_text.py --cfg <path_to_config_yaml_file> --repo_path <path-to-repo> [options]

Options:
    --cfg             Path to the config file 
    --repo_path       Path to the local GitHub repository (absolute or relative).
    -w, --max_words   Maximum number of words per output file (default: 200,000).
    -o, --output_dir  Directory to save the output files (default: current directory).
    --skip_patterns   Additional file patterns to skip (e.g., "*.md" "*.txt").
    --skip_dirs       Additional directories to skip.
    -v, --verbose     Enable verbose output.

Example:
    python repo_to_text.py --cfg config.yaml --repo_path ./my_repo -w 100000 -o ./output --skip_patterns "*.md" "*.txt" --skip_dirs "tests" -v
"""
import os
import nltk
import yaml
import fnmatch
import argparse
from pathlib import Path
from textwrap import dedent

nltk.download('punkt', quiet=True)
from nltk.tokenize import word_tokenize


def load_yaml(fname):
    # Load configuration from the YAML config file
    try:
        with open(fname, 'r') as config_file:
            config = yaml.safe_load(config_file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{fname}' not found.")
        config = {}
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        config = {}

    return config


class RepoContentProcessor:
    def __init__(self, repo_path, config_path={}, max_words=200000):
        # Convert relative path to absolute path
        self.repo_path = Path(repo_path).resolve()
        self.content = ""
        self.file_counter = 1
        self.current_word_count = 0
        self.MAX_WORDS = max_words
        
        config = load_yaml(config_path)

        # Define directories to skip
        self.skip_dirs = config.get("skip_dirs", [])
        # Define file patterns to skip
        self.skip_patterns = config.get("skip_patterns", [])

    def format_file_block(self, relative_path, file_content):
        """Format a file's content block with consistent indentation"""
        separator = "*" * 40
        return f"{separator}\n{relative_path}\n{separator}\n{file_content}\n{separator}\n"

    def count_words(self, text):
        """Count words in the given text using NLTK tokenizer"""
        return len(word_tokenize(text, language='english', preserve_line=True))
    
    def is_in_git_directory(self, path):
        """Check if the path is inside a .git directory"""
        parts = path.relative_to(self.repo_path).parts
        return '.git' in parts
    
    def should_skip_path(self, path):
        # Get parts of the relative path (e.g., ('node_modules', 'file.js'))
        try:
            relative_parts = path.relative_to(self.repo_path).parts
        except ValueError:
            # If path is not relative to repo_path, do not skip it.
            relative_parts = ()

        # Skip if any part of the path is in skip_dirs
        if any(part in self.skip_dirs for part in relative_parts):
            return True

        # Skip anything in .git directory
        if '.git' in relative_parts:
            return True

        # For files, also check if their own name matches any skip patterns.
        if path.is_file():
            if any(fnmatch.fnmatch(path.name, pattern) for pattern in self.skip_patterns):
                return True
        
        return False
    
    def save_current_content(self):
        """Save current content to a numbered file"""
        if self.content:
            output_file = f'repo_content_{self.file_counter}.txt'
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(self.content.rstrip() + "\n")  # Ensure single newline at end of file
            print(f"Created {output_file} with {self.current_word_count} words")
            self.file_counter += 1
            self.content = ""
            self.current_word_count = 0
    
    def process_file(self, file_path):
        """Process a single file and add its content to the accumulator"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read().rstrip()  # Remove trailing whitespace
            
            # Create the content block with consistent formatting
            relative_path = str(file_path.relative_to(self.repo_path))
            path_block = self.format_file_block(relative_path, file_content)
            
            # Count words in the new block
            block_word_count = self.count_words(path_block)
            
            # Check if adding this block would exceed the word limit
            if self.current_word_count + block_word_count > self.MAX_WORDS:
                self.save_current_content()
            
            # Add the new block with a single newline for separation
            if self.content:
                self.content += "\n"  # Add separator line only between blocks
            self.content += path_block
            self.current_word_count += block_word_count
            
        except (UnicodeDecodeError, IOError) as e:
            print(f"Skipping {file_path}: {str(e)}")
    
    def process_repo(self):
        """Process all files in the repository"""
        print(f"Processing repository at: {self.repo_path}")
        
        if not self.repo_path.exists():
            raise ValueError(f"Path does not exist: {self.repo_path}")
        
        file_count = 0
        skipped_count = 0
        skipped_dirs = set()
        
        # Use Path.rglob instead of os.walk for better path handling
        for file_path in self.repo_path.rglob('*'):
            try:
                # Skip if path should be skipped
                if self.should_skip_path(file_path):
                    if file_path.is_dir():
                        rel_path = file_path.relative_to(self.repo_path)
                        if str(rel_path) not in skipped_dirs:
                            print(f"Skipping directory: {rel_path}")
                            skipped_dirs.add(str(rel_path))
                    else:
                        skipped_count += 1
                    continue
                
                # Process only files, not directories
                if file_path.is_file():
                    print(f"Processing: {file_path.relative_to(self.repo_path)}")
                    self.process_file(file_path)
                    file_count += 1
                    
            except ValueError as e:
                print(f"Error processing path {file_path}: {e}")
                continue
        
        # Save any remaining content
        if self.content:
            self.save_current_content()
            
        print(f"\nProcessed {file_count} files, skipped {skipped_count} files")


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Process a GitHub repository and concatenate file contents with word limit.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '--cfg',
        type=str,
        default="config.yaml",
        help='Path to the config.yaml file'
    )
    
    parser.add_argument(
        '--repo_path',
        type=str,
        help='Path to the local GitHub repository (absolute or relative)'
    )
    
    parser.add_argument(
        '-w', '--max_words',
        type=int,
        default=200000,
        help='Maximum number of words per output file'
    )
    
    parser.add_argument(
        '-o', '--output_dir',
        type=str,
        default='.',
        help='Directory to save the output files'
    )
    
    parser.add_argument(
        '--skip_patterns',
        type=str,
        nargs='+',
        help='Additional file patterns to skip (e.g., "*.md" "*.txt")'
    )
    
    parser.add_argument(
        '--skip_dirs',
        type=str,
        nargs='+',
        help='Additional directories to skip'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    return parser.parse_args()


def validate_args(args):
    """Validate command line arguments"""
    # Convert relative path to absolute path
    repo_path = Path(args.repo_path).resolve()
    
    # Check if repo path exists and is a directory
    if not repo_path.exists():
        raise ValueError(f"Repository path does not exist: {repo_path}")
    if not repo_path.is_dir():
        raise ValueError(f"Repository path is not a directory: {repo_path}")
    
    # Check if output directory exists, create if it doesn't
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Validate max words
    if args.max_words <= 0:
        raise ValueError("Maximum words must be greater than 0")
    
    # Update args with resolved paths
    args.repo_path = repo_path
    args.output_dir = output_dir


def main():
    try:
        # Parse and validate arguments
        args = parse_arguments()
        validate_args(args)

        # except ValueError as e:
        #     print(f"Error: {e}")
        #     return 1

        # Create the processor (which loads the config file)
        processor = RepoContentProcessor(args.repo_path, args.cfg, args.max_words)

        # Now change to the output directory
        os.chdir(str(args.output_dir))

        # (Optionally update skip lists here, see below)
        if args.skip_patterns:
            # Use extend() if skip_patterns is a list
            processor.skip_patterns.extend(args.skip_patterns)
        if args.skip_dirs:
            processor.skip_dirs.extend(args.skip_dirs)

        processor.process_repo()
        return 0

    except Exception as e:
        print(f"Error during processing: {e}")
        return 1


if __name__ == "__main__":
    main()
