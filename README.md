# AI Response Validation System with Hallucination Detection Assistance

## 1. About the Project

Large Language Models (LLMs) can generate answers that sound convincing but may contain incorrect, misleading, or unsupported information. This is commonly known as AI hallucination.

This project aims to develop a system that evaluates AI-generated responses by comparing them with relevant reference information and assessing their quality and reliability.

The system is being developed as part of the Infosys Springboard Virtual Internship – Batch 5 (2026–27).

## 2. Problem Statement

It is difficult for users to independently verify whether an AI-generated response is factually correct, relevant, complete, and supported by reliable evidence.

This project aims to simplify that process through reference-based retrieval and automated response evaluation.

## 3. Project Objectives

- Evaluate the relevance of AI-generated responses.
- Assess factual accuracy using reference information.
- Identify potentially fabricated or unsupported claims.
- Check response completeness.
- Generate understandable evaluation results with supporting evidence.

## 4. System Architecture

The planned system workflow is:

1. User submits a question and AI-generated response.
2. Backend validates the submitted input.
3. Reference Knowledge Base retrieves relevant information.
4. Evaluation agents assess the response.
5. Verdict module combines evaluation results.
6. Results are presented to the user.

Refer to [architecture.png](architecture.png) for the system architecture diagram.

## 5. Evaluation Dimensions

| Dimension | Purpose |
|---|---|
| Relevance | Checks whether the response addresses the question |
| Accuracy | Assesses factual correctness |
| Hallucination Risk | Identifies unsupported or fabricated claims |
| Completeness | Checks whether important information is missing |

## 6. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend API |
| Pandas | Dataset processing |
| Hugging Face Datasets | Public benchmark datasets |
| Sentence Transformers | Text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Vector database |
| Git and GitHub | Version control |

## 7. Datasets

The reference knowledge base uses:

- **SQuAD:** Stanford Question Answering Dataset.
- **TruthfulQA:** Benchmark dataset for evaluating truthfulness in language models.

The datasets are cleaned, preprocessed, and divided into token-based chunks before embedding generation and vector indexing.

## 8. Implemented Features

The following components have been developed:

- Evaluation input validation.
- FastAPI evaluation input endpoint.
- Dataset inspection and preprocessing.
- Token-based text chunking.
- Embedding generation using Sentence Transformers.
- ChromaDB vector indexing.
- Semantic retrieval of reference information.
- Retrieval testing using representative benchmark questions.
- Integration of reference retrieval with the evaluation API.

## 9. Current Development Status

**Milestone 1 – Research, System Design and Initial Implementation**

The initial backend, reference knowledge base, and retrieval pipeline have been implemented and tested.

The evaluation agents, automated scoring, final verdict generation, and user interface are planned for subsequent development stages.

## 10. Project Structure

```text
Springboard-Virtual-Internship/
│
├── docs/
│   ├── dataset_inspection.md
│   ├── evaluation_methodology.md
│   ├── input_module_implementation.md
│   ├── literature_review.md
│   ├── problem_statement.md
│   ├── system_architecture.md
│   ├── system_design.md
│   └── technology_stack.md
│
├── src/
│   ├── input_module/
│   │   ├── api.py
│   │   └── input_handler.py
│   │
│   └── data_processing/
│       ├── inspect_datasets.py
│       ├── preprocess_datasets.py
│       ├── chunk_datasets.py
│       ├── knowledge_base.py
│       ├── retrieval.py
│       └── test_retrieval.py
│
├── architecture.png
├── .gitignore
└── README.md
```

## 11. Running the Backend

Install the required dependencies:

```bash
py -m pip install fastapi uvicorn pandas pyarrow sentence-transformers chromadb
```

Start the backend from the input module directory:

```bash
cd src/input_module
py -m uvicorn api:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

**Note:** The local datasets and ChromaDB files are excluded from GitHub. They must be prepared locally before testing the retrieval-integrated API.

## 12. Project Information

- **Program:** Infosys Springboard Virtual Internship – Batch 5 (2026–27)
- **Project:** Development of AI Response Validation System with Hallucination Detection Assistance
- **Developer:** Tanusha L