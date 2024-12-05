from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm_handler import get_context, generate_response

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/query")
async def process_query(query: Query):
    try:
        context = get_context(query.question)
        response = generate_response(query.question, context)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))