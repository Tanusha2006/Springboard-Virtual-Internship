# Dataset Collection and Inspection

## 1. SQuAD Dataset

Source: [Hugging Face – SQuAD](https://huggingface.co/datasets/rajpurkar/squad)

- Training records: 87,599
- Validation records: 10,570
- Columns: id, title, context, question, answers

Purpose: Used to evaluate whether AI-generated answers are supported by reference contexts.

## 2. TruthfulQA Dataset

Source: [Hugging Face – TruthfulQA](https://huggingface.co/datasets/leibni/truthful_qa)

- Records: 817
- Columns: type, category, question, best_answer, correct_answers, incorrect_answers, source

Purpose: Tests whether AI-generated answers avoid common misconceptions.

Note: This is a community-hosted Parquet version of TruthfulQA.

## 3. Inspection and Data Quality

- Total records: 98,986.
- All three Parquet files were loaded and inspected using Pandas.
- No missing values were found.
- Duplicate questions: SQuAD Training – 244; SQuAD Validation – 31; TruthfulQA – 0.

Repeated SQuAD questions were preserved because some have different valid answers.

## 4. Data Preprocessing

- Removed unnecessary leading and trailing spaces.
- Cleaned questions, contexts, titles and answers.
- Preserved repeated questions.
- Saved processed datasets separately from original files.

### Verification Results

| Dataset | Processed Records | Missing Values |
|---|---:|---:|
| SQuAD Training | 87,599 | 0 |
| SQuAD Validation | 10,570 | 0 |
| TruthfulQA | 817 | 0 |

All processed datasets were successfully reopened and verified.

## 5. Text Chunking

SQuAD training and validation contexts were divided into overlapping chunks.

- Chunk size: 200 tokens
- Overlap: 40 tokens
- Tokenizer: all-MiniLM-L6-v2 tokenizer

Chunk files were saved in `data/processed/chunks/`.

TruthfulQA was retained as structured question-answer data.

## 6. Vector Database and Retrieval Evaluation

### Configuration

- Embedding model: sentence-transformers/all-MiniLM-L6-v2
- Vector database: ChromaDB
- Distance metric: Cosine similarity
- Embeddings: Normalized
- Collection: `reference_knowledge_base`

### Indexed Dataset Distribution

| Dataset | Indexed Records |
|---|---:|
| SQuAD Training | 31,000 |
| SQuAD Validation | 200 |
| TruthfulQA | 200 |
| **Total** | **31,400** |

### Retrieval Evaluation

Six questions from TruthfulQA and SQuAD Validation were tested.

| Dataset | Questions | Passed |
|---|---:|---:|
| TruthfulQA | 3 | 3 |
| SQuAD Validation | 3 | 3 |
| **Total** | **6** | **6** |

**Observed success rate: 100% (6/6).**

The tests checked dataset matching and reference-answer presence in retrieved passages.

### Limitations

- Only a selected portion of the datasets was indexed.
- Retrieval testing covered six questions.
- Larger-scale retrieval evaluation is required to establish general retrieval quality.