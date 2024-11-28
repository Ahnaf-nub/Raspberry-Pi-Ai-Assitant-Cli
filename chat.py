from openai import OpenAI
import sys

# Replace the API key with your actual key
OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

# ANSI escape codes for terminal formatting
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

def format_response(response):
    # Replace single quotes with bold formatting
    formatted_response = response.replace("'", f"{BOLD}").replace("`", f"{BOLD}")
    return formatted_response

def ask_openai(query):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Provide answers considering the context of Raspberry Pi Zero 2W and give the answers in one line unless essential."},
        {
            "role": "user",
            "content": query
        }
    ]
    try:
        print(f"{BLUE}{BOLD}Query:{RESET} {query}\n")
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        response = completion.choices[0].message.content.strip()
        formatted_response = format_response(response)
        print(f"{GREEN}{BOLD}Response:{RESET} {formatted_response}")
    except Exception as e:
        print(f"{RED}{BOLD}Error:{RESET} {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        ask_openai(query)
    else:
        print(f"{YELLOW}{BOLD}Usage:{RESET} Provide a query as a command-line argument.")