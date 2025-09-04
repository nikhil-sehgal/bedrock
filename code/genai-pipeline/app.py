from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="YOUR_OPENAI_KEY")

def genai_pipeline(query: str):
    # Step 1: Preprocess
    cleaned = query.strip()
    
    # Step 2: LLM call
    template = PromptTemplate.from_template("Answer this professionally: {q}")
    prompt = template.format(q=cleaned)
    response = llm(prompt)
    
    # Step 3: Postprocess
    return response.strip()

if __name__ == "__main__":
    print(genai_pipeline("explain AI pipelines"))
