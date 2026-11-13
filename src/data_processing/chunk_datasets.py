
import pandas as pd
from pathlib import Path
from transformers import AutoTokenizer

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
CHUNK_DIR = PROCESSED_DIR / "chunks"
CHUNK_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 200
OVERLAP = 40

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def create_chunks(text):
    if not isinstance(text, str) or not text.strip():
        return []

    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    chunks = []
    start = 0

    while start < len(token_ids):
        end = min(start + CHUNK_SIZE, len(token_ids))

        chunk_ids = token_ids[start:end]

        chunk_text = tokenizer.decode(
            chunk_ids,
            skip_special_tokens=True
        )

        chunks.append(chunk_text)

        if end == len(token_ids):
            break

        start = end - OVERLAP

    return chunks


def chunk_squad(input_file, output_file):
    input_path = PROCESSED_DIR / input_file
    output_path = CHUNK_DIR / output_file

    df = pd.read_parquet(input_path)
    chunk_records = []

    for _, row in df.iterrows():
        chunks = create_chunks(row["context"])
        answers = row["answers"]

        answer_texts = (
            answers.get("text", [])
            if isinstance(answers, dict)
            else []
        )

        for index, chunk in enumerate(chunks):
            answer_present = any(
                answer in chunk
                for answer in answer_texts
                if isinstance(answer, str) and answer
            )

            chunk_records.append({
                "id": row["id"],
                "title": row["title"],
                "question": row["question"],
                "chunk_id": index,
                "chunk_text": chunk,
                "answers": answers,
                "answer_present": answer_present
            })

    chunk_df = pd.DataFrame(chunk_records)
    chunk_df.to_parquet(output_path, index=False)

    print("\nDataset:", input_file)
    print("Original records:", len(df))
    print("Generated chunks:", len(chunk_df))
    print("Saved to:", output_path)


chunk_squad(
    "squad_train_processed.parquet",
    "squad_train_chunks.parquet"
)

chunk_squad(
    "squad_validation_processed.parquet",
    "squad_validation_chunks.parquet"
)

print("\nTOKEN-BASED CHUNKING COMPLETED!")

print("\nCHUNK VERIFICATION")

for file_path in CHUNK_DIR.glob("*.parquet"):
    df = pd.read_parquet(file_path)

    print("\nFile:", file_path.name)
    print("Total chunks:", len(df))
    print("Missing values:", df.isnull().sum().sum())

    if not df.empty:
        sample = df.iloc[0]["chunk_text"]
        print("Sample chunk:", sample[:300])
        print(
            "Sample token count:",
            len(tokenizer.encode(sample, add_special_tokens=False))
        )
