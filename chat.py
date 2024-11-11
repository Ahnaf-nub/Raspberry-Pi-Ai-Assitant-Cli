from openai import OpenAI
OPENAI_API_KEY = ""

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_openai():
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Provide answers considering the context of Raspberry Pi Zero 2W and give the answers in one line unless essential."},
        {
            "role": "user",
            "content": input("Ask: ")
        }
    ]
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    print(completion.choices[0].message.content.strip())

if __name__ == "__main__":
    ask_openai()
