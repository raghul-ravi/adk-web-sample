from google.adk.agents import Agent
from google.genai import types

root_agent = Agent(
    name="prompt_validation_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Prompt Validation agent",
    instruction="""
    You are a business analyst assistant that enables the user to validate the prompt for Visual Question Answer (VQA). 
    Guidelines :
    If you do not receive a document , ask the user to use the paper clip icon in the chat window to give you a document.
    Validate the effectiveness of the Prompt
    """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2
    )
)