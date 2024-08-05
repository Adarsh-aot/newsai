# Project Title

AI Trend Analysis and Article Generation

## Introduction

This project leverages the CrewAI framework to automate the process of researching and writing insightful articles on the latest trends in AI. It utilizes two specialized agents, a researcher and a writer, to perform these tasks efficiently. The agents are configured to operate sequentially, ensuring a smooth workflow from research to content creation.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai-trend-analysis.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ai-trend-analysis
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up environment variables:
    Create a `.env` file in the project root and add your GROQ API key:
    ```
    GROQ_API_KEY=your_api_key_here
    SERPER_API_KEY=your_api_key_here
    ```

## Usage

To start the AI trend analysis and article generation process, execute the following command:
```sh
python crew.py
```
The script will prompt you to input a topic, for example, "AI in healthcare".

## Features

- **Automated Research**: Uses a senior researcher agent to uncover groundbreaking technologies and trends in the specified topic.
- **Article Writing**: Generates a comprehensive and engaging article based on the research findings.
- **Sequential Workflow**: Ensures a streamlined process from research to writing with enhanced feedback mechanisms.
- **Customizable Output**: Allows configuration of output files and formats.

## Dependencies

- Python 3.x
- CrewAI
- Langchain_Groq
- dotenv

## Configuration

The agents and tasks are configured in the following scripts:

- `agent.py`: Defines the research and writer agents, including their roles, goals, and tools.
- `task.py`: Specifies the tasks for researching and writing, detailing the expected outputs and configurations.
- `crew.py`: Sets up the Crew with agents and tasks, and starts the execution process.

### Example Configuration

```python
# agent.py
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

research = Agent(
    role="Senior Researcher",
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
```

## Examples

### Research Task

The research task is defined to identify the next big trend in the given topic, focusing on pros, cons, and the overall narrative.

```python
# task.py
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=research,
)
```

### Writing Task

The writing task composes an insightful article on the specified topic, ensuring it is easy to understand, engaging, and positive.

```python
# task.py
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='new-blog-post.md'
)
```

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are installed correctly.
2. Verify that your GROQ API key is correctly set in the `.env` file.
3. Check for any syntax errors in the configuration scripts.

## Contributors

- **Your Name** - *Initial work* - [YourGithubUsername](https://github.com/yourgithubusername)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.