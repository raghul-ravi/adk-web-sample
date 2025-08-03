# ADK Web Sample - Prompt Validation Agent

This project contains a Google ADK agent designed to validate prompts for Visual Question Answer (VQA) tasks.

## Project Structure

```
adk-web-sample/
├── prompt_validation_agent/     # ADK agent package
│   ├── __init__.py             # Package initialization
│   ├── agent.py                # Agent definition (root_agent)
│   ├── example.prompt          # Example prompt file
│   └── sample_closing_document.pdf  # Sample document
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image configuration
└── docker-compose.yml          # Docker compose configuration
```

## Agent Description

The Prompt Validation Agent is a business analyst assistant that helps users validate prompts for Visual Question Answer (VQA) tasks. It uses the Gemini 2.0 Flash model with a temperature of 0.2 for consistent responses.

## Prerequisites

- Python 3.10+
- Google API Key (for Gemini API access)
- Docker (optional, for containerized deployment)

## Installation

### Local Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install google-adk
```

3. Set your Google API key:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

### Docker Setup

1. Build the Docker image:
```bash
docker build -t adk-web-sample .
```

2. Run with Docker Compose:
```bash
# Set your API key in environment
export GOOGLE_API_KEY="your-api-key-here"

# Run the container
docker-compose up
```

Or run directly with Docker:
```bash
docker run -p 8000:8000 -e GOOGLE_API_KEY="your-api-key-here" adk-web-sample
```

## Running the Agent

### Local Development

From the project root directory (adk-web-sample), run:
```bash
adk web
```

The web interface will be available at http://localhost:8000

### Docker

After starting the container, access the web interface at http://localhost:8000

## Usage

1. Open the ADK web interface
2. Select "prompt_validation_agent" from the dropdown menu
3. Upload a document using the paperclip icon in the chat window
4. Ask the agent to validate your VQA prompts

## Features

- Document upload support for VQA context
- Prompt effectiveness validation
- Business analyst assistance for VQA tasks
- Web-based interactive interface

## Dependencies

- google-adk: ADK framework for building AI agents
- google-genai: Google Generative AI library for Gemini models

## Notes

- Always run ADK commands from the parent directory (adk-web-sample), not from inside the agent directory
- The agent expects documents to be uploaded via the chat interface for VQA validation
- The Docker setup includes volume mounting for development, allowing real-time code changes