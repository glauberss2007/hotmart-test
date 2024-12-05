from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from text_processor import process_text, store_in_qdrant

app = FastAPI()

class Document(BaseModel):
    text: str

@app.post("/process")
async def process_document(document: Document):
    try:
        embeddings, sentences = process_text(document.text)
        store_in_qdrant(embeddings, sentences)
        return {"message": "Document processed and stored successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))