import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

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
    
def print_usage_info(completion, messages, verbose=False):
    if completion.usage:
        prompt_tokens = completion.usage.prompt_tokens
        response_tokens = completion.usage.completion_tokens

        if verbose:
            print("User prompt:", messages[0]["content"])
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
        
        print("Response: ")
        print(completion.choices[0].message.content)
            
    else:
        raise ValueError("No usage information returned from the API.")

def main():
    api_key = get_api_key()
    
    user_prompt, verbose = get_user_prompt()
    
    client = create_client(api_key)
    
    messages=[
    {
        "role": "user",
        "content": user_prompt,
    }
]
    
    completion = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    
    print_usage_info(completion, messages, verbose)

if __name__ == "__main__":
    main()
