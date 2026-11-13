
import pandas as pd
from pathlib import Path


# Define dataset folders
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

# Create processed folder if it does not exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# Remove unnecessary spaces from text
def clean_text(value):
    if isinstance(value, str):
        return value.strip()
    return value


# Clean SQuAD dataset
def preprocess_squad(file_path, output_name):

    df = pd.read_parquet(file_path)

    # Clean text columns
    text_columns = ["id", "title", "context", "question"]

    for column in text_columns:
        df[column] = df[column].apply(clean_text)

    # Clean answer text while preserving answer positions
    def clean_answers(answers):
        if isinstance(answers, dict):
            answers = answers.copy()
            answers["text"] = [
                clean_text(answer)
                for answer in answers["text"]
            ]
        return answers

    df["answers"] = df["answers"].apply(clean_answers)

    # Save processed dataset
    output_path = PROCESSED_DIR / output_name
    df.to_parquet(output_path, index=False)

    print(output_name, "processed successfully.")
    print("Records:", len(df))


# Clean TruthfulQA dataset
def preprocess_truthfulqa(file_path, output_name):

    df = pd.read_parquet(file_path)

    # Clean text columns
    text_columns = [
        "type",
        "category",
        "question",
        "best_answer",
        "source"
    ]

    for column in text_columns:
        df[column] = df[column].apply(clean_text)

    # Clean lists of correct and incorrect answers
    for column in ["correct_answers", "incorrect_answers"]:
        df[column] = df[column].apply(
            lambda answers: [
                clean_text(answer) for answer in answers
            ]
        )

    # Save processed dataset
    output_path = PROCESSED_DIR / output_name
    df.to_parquet(output_path, index=False)

    print(output_name, "processed successfully.")
    print("Records:", len(df))


# Process SQuAD datasets
preprocess_squad(
    RAW_DIR / "train-00000-of-00001.parquet",
    "squad_train_processed.parquet"
)

preprocess_squad(
    RAW_DIR / "validation-00000-of-00001.parquet",
    "squad_validation_processed.parquet"
)


# Process TruthfulQA dataset
preprocess_truthfulqa(
    RAW_DIR / "new validation-00000-of-00001.parquet",
    "truthfulqa_processed.parquet"
)


print("\nAll datasets have been preprocessed successfully.")

# Verify processed datasets

print("\nPROCESSED DATASET VERIFICATION")

for file_path in PROCESSED_DIR.glob("*.parquet"):

    df = pd.read_parquet(file_path)

    print("\nFile:", file_path.name)
    print("Records:", len(df))
    print("Missing values:", df.isnull().sum().sum())