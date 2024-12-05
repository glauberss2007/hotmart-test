from transformers import GPTJForCausalLM, AutoTokenizer
from qdrant_client import QdrantClient

model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
client = QdrantClient("qdrant", port=6333)

def get_context(question):
    # Generate embedding for the question
    question_embedding = model.encode([question])[0]
    
    # Search Qdrant for similar contexts
    search_result = client.search(
        collection_name="documents",
        query_vector=question_embedding.tolist(),
        limit=3  # Get top 3 most relevant sentences
    )
    
    # Extract and return the relevant sentences
    context = " ".join([hit.payload["sentence"] for hit in search_result])
    return context

def generate_response(question, context):
    # Prepare input for the LLM
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    
    # Generate response using GPT-J
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response