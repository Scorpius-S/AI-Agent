import os
import sys
import argparse
from dotenv import load_dotenv
import google.generativeai as genai
from functions.get_files_info import schema_get_files_info
import google.generativeai.types as types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

parser = argparse.ArgumentParser(description="Generate AI content using Gemini.")
parser.add_argument("prompt", help="User prompt for the generation")
parser.add_argument("--verbose", help="Enable verbose output", action="store_true")
args = parser.parse_args()
user_prompt = args.prompt

messages = [
    {
        "role": "user",
        "parts": [{"text": f"{user_prompt} Use one paragraph."}]
    }
]


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

model = genai.GenerativeModel(
    'gemini-2.0-flash-001',
    system_instruction=system_prompt
)

available_functions = types.Tool(function_declarations=[schema_get_files_info])
config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt)
response = model.generate_content(contents=messages,generation_config=config)

if function_call_part := response.function_calls:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
else:
    print(response.text)
if args.verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")