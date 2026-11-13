
from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parents[2]
VECTOR_DB_DIR = BASE_DIR / "data" / "vector_db"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "reference_knowledge_base"

print("Loading retrieval model...")
model = SentenceTransformer(MODEL_NAME)

print("Connecting to ChromaDB...")
client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))
collection = client.get_collection(COLLECTION_NAME)


def retrieve_reference_context(question, top_k=5):
    question_embedding = model.encode(
        [question],
        normalize_embeddings=True
    )

    results = collection.query(
        query_embeddings=question_embedding.tolist(),
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    retrieved_context = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        retrieved_context.append({
            "text": document,
            "dataset": metadata.get("dataset"),
            "source_question": metadata.get("question"),
            "distance": float(distance)
        })

    return retrieved_context
