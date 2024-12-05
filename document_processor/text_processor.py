from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

model = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient("qdrant", port=6333)

def process_text(text):
    # Tokenize and generate embeddings
    sentences = text.split('.')  # Simple sentence splitting
    embeddings = model.encode(sentences)
    return embeddings, sentences

def store_in_qdrant(embeddings, sentences):
    # Store embeddings in Qdrant
    client.recreate_collection(
        collection_name="documents",
        vectors_config=VectorParams(size=embeddings[0].shape[0], distance=Distance.COSINE),
    )
    
    points = []
    for i, embedding in enumerate(embeddings):
        point = {
            "id": i,
            "vector": embedding.tolist(),
            "payload": {
                "sentence": sentences[i]
            }
        }
        points.append(point)
    
    client.upsert(
        collection_name="documents",
        points=points,
    )