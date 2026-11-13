
import pandas as pd
from pathlib import Path

# Project data folder
DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

# Dataset file paths
datasets = {
    "SQuAD Training": DATA_DIR / "train-00000-of-00001.parquet",
    "SQuAD Validation": DATA_DIR / "validation-00000-of-00001.parquet",
    "TruthfulQA": DATA_DIR / "new validation-00000-of-00001.parquet"}

# Inspect each dataset
for name, file_path in datasets.items():

    print("\n" + "=" * 50)
    print(f"DATASET: {name}")
    print("=" * 50)

    if file_path.exists():
        df = pd.read_parquet(file_path)

        print("Number of records:", len(df))
        print("Columns:", df.columns.tolist())

        print("\nFirst record:")
        print(df.iloc[0].to_dict())

    else:
        print("File not found:", file_path)
