
**User Prompt**

Can you provide a feature exploration guide for this codebase? Outline any optional features, hidden modules, or ‘nice-to-have’ functionalities that may not be immediately obvious but could be valuable. Include a brief description of each feature, its purpose, and examples of how it might enhance or extend the core functionalities of the codebase.

---

**Gemini Response**

Here is a guide for exploring optional or hidden features in this codebase, based on the provided source code snippets. 

### Feature Exploration Guide:

*   **Telemetry for Feature Prioritization and Improvement:** CrewAI incorporates an anonymous telemetry system to gather usage data. This data aids in understanding user behavior, feature adoption, and areas needing improvement. 

    *   **Purpose:** Guide development efforts, identify popular features, understand usage patterns, and optimize resource allocation.
    *   **Examples:** Track agent memory and delegation usage, parallel vs. sequential task execution, and language model preferences to inform future development and support.
*   **`share_crew` Feature for Enhanced Insights:** An opt-in feature called `share_crew` allows users to share more detailed usage data with CrewAI, including task descriptions and agent attributes. 
    *   **Purpose:** Provide richer insights into how CrewAI is used, enabling more targeted improvements and a deeper understanding of user workflows.
    *   **Examples:** Help CrewAI identify common use cases, design better tools and integrations, and create more relevant examples and documentation.
*   **Experimental RAG Search Tools:** Several Retrieval-Augmented Generation (RAG) search tools, still in experimental stages, offer specialized search capabilities for different data sources. 
    *   **Purpose:** Enable agents to access and extract information from various sources, enhancing their research and decision-making abilities.
    *   **Examples:** The `WebsiteSearchTool` performs semantic searches on websites. The `CodeDocsSearchTool` searches code documentation, while the `JSONSearchTool` focuses on searching within JSON file contents.  The `MDXSearchTool` extracts information from MD files using query-based searches, and the `PGSearchTool` queries PostgreSQL databases.
*   **Custom Model and Embeddings Configuration:** Many tools allow customization of the underlying language model (LLM) and embedding models used for processing and analysis. 
    *   **Purpose:** Cater to specific performance, accuracy, or cost requirements by selecting different providers (OpenAI, Google, Ollama, etc.) and model configurations.
    *   **Examples:** Configure an LLM with specific parameters like temperature, top_p, and streaming for text generation, or select a specialized embedding model from a specific provider.
*   **Advanced Tool Parameters for Fine-grained Control:**  Tools offer optional parameters for customizing their behavior beyond basic functionality. 
    *   **Purpose:** Enhance flexibility, enable advanced use cases, and handle specific scenarios more effectively.
    *   **Examples:** The `SeleniumScrapingTool` includes options like `cookie` for simulating logged-in sessions and `wait_time` for handling dynamic content on websites.
*   **Crew Configuration Options:**  The `Crew` class supports various configuration options that affect the overall crew execution. 
    *   **Purpose:** Control aspects like execution process (sequential or parallel), logging, planning, maximum requests per minute, and the use of prompt files.
    *   **Examples:** Set `planning` to `True` to enable automatic planning of crew execution. Define a `max_rpm` limit to control the rate of requests during execution.
*   **Task-Specific Tool Limiting:** When defining a `Task`, you can provide a list of `tools` that the agent assigned to the task is allowed to use.
    *   **Purpose:**  Restrict an agent's access to tools within the context of a particular task, enhancing security and control.
    *   **Examples:** If an agent has access to both a web search tool and a database tool, you can limit it to only using the database tool for a specific task that involves internal data analysis.

Please note that the information provided in this guide is based solely on the source code snippets you provided.  Further investigation of the full codebase may reveal additional features and functionalities.  It is always recommended to refer to the complete codebase and documentation for a comprehensive understanding of the software's capabilities. 

