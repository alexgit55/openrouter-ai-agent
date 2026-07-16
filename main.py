import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
import prompts
import call_function
import json

def get_api_key():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")
    return api_key

def get_user_prompt():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args.user_prompt, args.verbose

def create_client(api_key):
    return OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )
    
def print_usage_info(response, messages, verbose=False):
    if response.usage:
        prompt_tokens = response.usage.prompt_tokens
        response_tokens = response.usage.completion_tokens

        if verbose:
            print("User prompt:", messages[1]["content"])
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
        
        print("Response: ")
        if response.choices[0].message.tool_calls:
            for tool_call in response.choices[0].message.tool_calls:
                result_message = call_function.call_function(tool_call=tool_call, verbose=verbose )
                if not result_message["content"]:
                    raise Exception(f"Error: No response received from request")
                if verbose:
                    print(f"-> {result_message['content']}")
                else:
                    print(f"{result_message['content']}")
                
        else:
            print(response.choices[0].message.content)
    else:
        raise ValueError("No usage information returned from the API.")

def main():
    api_key = get_api_key()
    
    user_prompt, verbose = get_user_prompt()
    
    client = create_client(api_key)
    
    messages=[
        {
            "role": "system",
            "content": prompts.system_prompt    
        },
        {
            "role": "user",
            "content": user_prompt,
        }
]
    
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=call_function.available_functions
    )
    
    print_usage_info(response, messages, verbose)

if __name__ == "__main__":
    main()
