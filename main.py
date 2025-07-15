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

model = genai.GenerativeModel('gemini-2.0-flash-001')
system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
model = genai.GenerativeModel(
    'gemini-2.0-flash-001',
    system_instruction=system_prompt
)
response = model.generate_content(contents=messages)

available_functions = types.tools(funtion_declarations=[schema_get_files_info])

print(response.text)
if args.verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")