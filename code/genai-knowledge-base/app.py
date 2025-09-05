from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Initialize embeddings & LLM
embeddings = OpenAIEmbeddings(openai_api_key="YOUR_OPENAI_KEY")
llm = OpenAI(openai_api_key="YOUR_OPENAI_KEY")

# Sample documents
docs = [
    "AI adoption in enterprises improves productivity.",
    "Amazon Bedrock provides enterprise-ready foundation models.",
    "Custom knowledge bases are built with embeddings + RAG."
]

# Step 1: Split
splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=10)
texts = splitter.split_text(" ".join(docs))

# Step 2: Embed + Store
db = FAISS.from_texts(texts, embeddings)

# Step 3: Query
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

if __name__ == "__main__":
    query = "What is Amazon Bedrock?"
    print("Answer:", qa.run(query))
