from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_KEY")

def text_to_sql(query: str):
    prompt = f"Convert this query to SQL: {query}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    query = "Show top 10 sales this month"
    print("Generated SQL:", text_to_sql(query))
