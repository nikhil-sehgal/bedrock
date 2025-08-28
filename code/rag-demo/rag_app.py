from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Step 1: Build embeddings
docs = [
    "Amazon Bedrock is AWS’s GenAI service.",
    "Agentic AI enables autonomous workflows.",
    "Map servers serve geospatial tiles to clients."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)

# Step 2: Store in FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Step 3: Query
query = "What is Bedrock?"
q_embedding = model.encode([query])
D, I = index.search(np.array(q_embedding), k=1)

print("Query:", query)
print("Best Match:", docs[I[0][0]])
