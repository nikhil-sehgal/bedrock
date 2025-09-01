from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/summarize")
def summarize(query: Query):
    # Mock GenAI summarizer
    summary = query.text[:50] + "..."
    return {"summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
