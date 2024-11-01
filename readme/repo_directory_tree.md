```prompt
Generate a directory tree of the repo in ascii format 
````

```response
Here is a directory tree in ASCII format that represents the repo:

```
├── src
│   ├── crewai
│   │   ├── cli
│   │   │   ├── authentication
│   │   │   │   └── utils.py
│   │   │   ├── __init__.py
│   │   │   ├── telemetry.py
│   │   │   ├── project_template
│   │   │   │   └── utils.py
│   │   │   ├── templates
│   │   │   │   ├── __init__.py
│   │   │   │   ├── crew
│   │   │   │   │   ├── pyproject.toml
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── src
│   │   │   │   │       ├── config
│   │   │   │   │       │   └── tasks.yaml
│   │   │   │   │       ├── crew.py
│   │   │   │   │       └── __init__.py
│   │   │   │   ├── flow
│   │   │   │   │   ├── pyproject.toml
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── src
│   │   │   │   │       ├── config
│   │   │   │   │       │   └── tasks.yaml
│   │   │   │   │       ├── crews
│   │   │   │   │       │   └── poem_crew
│   │   │   │   │       │       ├── config
│   │   │   │   │       │       │   └── tasks.yaml
│   │   │   │   │       │       └── crew.py
│   │   │   │   │       ├── flow.py
│   │   │   │   │       └── __init__.py
│   │   │   │   ├── tool
│   │   │   │   │   ├── pyproject.toml
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── src
│   │   │   │   │       ├── {{folder_name}}
│   │   │   │   │       │   └── {{class_name}}.py
│   │   │   │   │       └── __init__.py
│   │   │   │   └── pipeline_router
│   │   │   │       ├── pyproject.toml
│   │   │   │       ├── README.md
│   │   │   │       └── src
│   │   │   │           ├── pipelines
│   │   │   │           │   ├── pipeline_normal.py
│   │   │   │           │   ├── pipeline_classifier.py
│   │   │   │           │   └── pipeline_urgent.py
│   │   │   │           ├── crews
│   │   │   │           │   ├── normal_crew
│   │   │   │           │   │   ├── config
│   │   │   │           │   │   │   └── tasks.yaml
│   │   │   │           │   │   └── crew.py
│   │   │   │           │   ├── classifier_crew
│   │   │   │           │   │   ├── config
│   │   │   │           │   │   │   └── tasks.yaml
│   │   │   │           │   │   └── crew.py
│   │   │   │           │   └── urgent_crew
│   │   │   │           │       ├── config
│   │   │   │           │       │   └── tasks.yaml
│   │   │   │           │       └── crew.py
│   │   │   │           ├── __init__.py
│   │   │   │           └── main.py
│   │   │   ├── utils.py
│   │   │   ├── constants.py
│   │   │   ├── git.py
│   │   │   └── exceptions.py
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── tasks
│   │   │   └── output_format.py
│   │   ├── process.py
│   │   └── crew.py
│   └── my_project
│       ├── src
│       │   ├── my_project
│       │   │   └── __init__.py
│       │   └── __init__.py
│       ├── .gitignore
│       ├── pyproject.toml
│       └── README.md
├── tests
│   └── cli
│       └── cli_test.py
└── docs
    └── tools
        ├── TXTSearchTool.md
        ├── FileReadTool.md
        └── DirectoryReadTool.md

```

The directory structure reveals:

- The main source code is in `src/crewai`. 
    - It includes components for a command-line interface (`cli`), the core logic (`agent.py`, `process.py`, `crew.py`), and task management (`tasks/`).
- The `my_project` folder appears to be a sample project generated using crewAI.
- Unit tests are located in `tests/cli/cli_test.py`.
- Documentation for various tools is organized in `docs/tools`.

**Key Concepts from the File Names and Structure**

- **AI Agents:** The file `agent.py` likely defines the structure and behavior of individual AI agents within the crewAI framework. 
- **Crews:** The `crew.py` file and the `crews` directories suggest that multiple AI agents can be grouped into crews for collaborative tasks.
- **Processes:** The file `process.py` likely defines the workflow or processes that these crews engage in to achieve their objectives. 
- **Tools:**  Files like `TXTSearchTool.md` and directories like `src/crewai/cli/templates/tool` indicate the presence of different tools that can be used by agents or crews within tasks.
- **Configuration:**  The `config` folders within crews suggest customizable settings and parameters for specific tasks and agents.
- **Pipeline:** The `pipelines` directory and files like `pipeline_normal.py` suggest a structured way to define and execute workflows or sequences of tasks within crewAI.
- **Telemetry:** The file `telemetry.py` suggests the framework includes features for collecting and analyzing data about crew performance and usage.

The information provided in the sources is not sufficient to determine the programming language used for this project. 
```