from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_KEY")

def enterprise_summary(topic: str):
    prompt = f"Explain how enterprises are adopting AI in {topic}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(enterprise_summary("banking"))
