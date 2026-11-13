
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

# Project paths
BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
CHUNK_DIR = PROCESSED_DIR / "chunks"
VECTOR_DB_DIR = BASE_DIR / "data" / "vector_db"

# Settings
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "reference_knowledge_base"

SAMPLE_SIZE = 200
BATCH_SIZE = 16
EMBEDDING_BATCH_SIZE = 8


def safe_text(value):
    if value is None:
        return ""

    if isinstance(value, float) and pd.isna(value):
        return ""

    return str(value).strip()


def safe_list(value):
    if isinstance(value, (list, tuple)):
        return [
            safe_text(item)
            for item in value
            if safe_text(item)
        ]
    return []


print("Connecting to ChromaDB...")

client = chromadb.PersistentClient(
    path=str(VECTOR_DB_DIR)
)

# Preserve the existing collection
try:
    collection = client.get_collection(COLLECTION_NAME)
    print("Existing collection found.")

except Exception:
    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )
    print("New collection created.")

print("Existing records:", collection.count())


# Load only the required datasets
print("\nReading SQuAD validation data...")

validation_path = CHUNK_DIR / "squad_validation_chunks.parquet"
validation_df = pd.read_parquet(validation_path).head(SAMPLE_SIZE)

print("Validation sample:", len(validation_df))

print("\nReading TruthfulQA data...")

truthfulqa_path = PROCESSED_DIR / "truthfulqa_processed.parquet"
truthfulqa_df = pd.read_parquet(truthfulqa_path).head(SAMPLE_SIZE)

print("TruthfulQA sample:", len(truthfulqa_df))


# Prepare records
records = []

# SQuAD validation
for row in validation_df.itertuples(index=False):

    question = safe_text(row.question)
    chunk_text = safe_text(row.chunk_text)

    if not chunk_text:
        continue

    record_id = (
        f"squad_validation_{row.id}_{row.chunk_id}"
    )

    embedding_text = (
        f"Question: {question}\n"
        f"Reference context: {chunk_text}"
    )

    metadata = {
        "dataset": "squad_validation",
        "source_id": safe_text(row.id),
        "title": safe_text(row.title),
        "question": question,
        "chunk_id": int(row.chunk_id),
        "answer_present": bool(row.answer_present)
    }

    records.append({
        "id": record_id,
        "document": chunk_text,
        "embedding_text": embedding_text,
        "metadata": metadata
    })


# TruthfulQA
for index, row in truthfulqa_df.iterrows():

    question = safe_text(row["question"])
    best_answer = safe_text(row["best_answer"])

    correct_answers = safe_list(row["correct_answers"])

    if not question:
        continue

    answers_text = " ".join(correct_answers)

    document = (
        f"Question: {question}\n"
        f"Best answer: {best_answer}\n"
        f"Correct answers: {answers_text}"
    )

    metadata = {
        "dataset": "truthfulqa",
        "source_id": str(index),
        "category": safe_text(row["category"]),
        "question": question,
        "source": safe_text(row["source"])
    }

    records.append({
        "id": f"truthfulqa_{index}",
        "document": document,
        "embedding_text": document,
        "metadata": metadata
    })


# Load embedding model
print("\nLoading embedding model...")

model = SentenceTransformer(MODEL_NAME)

# Add only records that are not already present
added = 0
skipped = 0

print("\nStarting safe indexing...")

for start in range(0, len(records), BATCH_SIZE):

    batch = records[start:start + BATCH_SIZE]

    batch_ids = [record["id"] for record in batch]

    existing = collection.get(ids=batch_ids)
    existing_ids = set(existing["ids"])

    new_records = [
        record for record in batch
        if record["id"] not in existing_ids
    ]

    skipped += len(batch) - len(new_records)

    if not new_records:
        continue

    embeddings = model.encode(
        [record["embedding_text"] for record in new_records],
        batch_size=EMBEDDING_BATCH_SIZE,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    collection.add(
        ids=[record["id"] for record in new_records],
        documents=[record["document"] for record in new_records],
        metadatas=[record["metadata"] for record in new_records],
        embeddings=embeddings.tolist()
    )

    added += len(new_records)

    print(
        f"New records added: {added} | "
        f"Already present: {skipped}"
    )


# Final verification
print("\n========== KNOWLEDGE BASE SUMMARY ==========")

print("New records added:", added)
print("Existing records skipped:", skipped)
print("Total records now:", collection.count())

print("\nDataset distribution:")

for dataset_name in [
    "squad_train",
    "squad_validation",
    "truthfulqa"
]:

    result = collection.get(
        where={"dataset": dataset_name},
        include=[]
    )

    print(f"{dataset_name}: {len(result['ids'])}")

print("\nSample indexed record:")

sample = collection.peek(limit=1)

if sample["ids"]:
    print("ID:", sample["ids"][0])
    print("Document:", sample["documents"][0][:300])
    print("Metadata:", sample["metadatas"][0])

print("\nSAFE INDEXING COMPLETED!")
