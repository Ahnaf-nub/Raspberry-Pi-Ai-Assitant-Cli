from openai import OpenAI
import sys
OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_openai(query):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Provide answers considering the context of Raspberry Pi Zero 2W and give the answers in one line unless essential."},
        {
            "role": "user",
            "content": query
        }
    ]
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    print(completion.choices[0].message.content.strip())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        ask_openai(query)
    else:
        print("Please provide a query.")
