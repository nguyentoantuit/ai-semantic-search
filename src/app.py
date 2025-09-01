from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("sentence-transformers/msmarco-distilbert-base-tas-b")

@app.post("/embed")
async def embed(request: Request):
    data = await request.json()
    sentences = data.get("sentences", [])
    embeddings = model.encode(sentences).tolist()
    return {"embeddings": embeddings}
