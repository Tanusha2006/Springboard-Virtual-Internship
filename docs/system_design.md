# System Design

## 1. System Architecture

The system evaluates AI-generated responses using reference knowledge retrieval and specialized evaluation agents.

**Main Components:**
1. User Interface
2. Evaluation Input Module
3. FastAPI Backend
4. Evaluation Orchestrator
5. Reference Knowledge Base (ChromaDB)
6. Retrieval Module
7. Four Judge Agents
8. Verdict Agent
9. Results Module

## 2. Agent Responsibilities

| Agent | Responsibility |
|---|---|
| Evaluation Orchestrator | Coordinates the evaluation workflow |
| Relevance Judge | Checks whether the response addresses the question |
| Accuracy Judge | Evaluates factual correctness against available evidence |
| Hallucination Detection Agent | Identifies unsupported or fabricated claims |
| Completeness Judge | Checks whether important information is missing |
| Verdict Agent | Combines evaluation results and generates the final verdict |

## 3. Evaluation Dimensions

Each dimension uses a scale of 0–5.

| Dimension | Scoring Direction |
|---|---|
| Relevance | Higher score = better relevance |
| Accuracy | Higher score = better accuracy |
| Hallucination Risk | Higher score = greater risk |
| Completeness | Higher score = better completeness |

### Initial Weighted Scoring Formula

Overall Score =

(0.25 × Relevance) +  
(0.35 × Accuracy) +  
(0.25 × (5 − Hallucination Risk)) +  
(0.15 × Completeness)

Percentage Score = Overall Score × 20

The weights are initial design choices and will be reviewed during testing.

## 4. Agent Orchestration Flow

1. User submits a question and AI-generated response.
2. Input Module validates the submission.
3. Evaluation Orchestrator receives the validated input.
4. Retrieval Module retrieves relevant evidence from ChromaDB.
5. Four judge agents independently evaluate the response.
6. Verdict Agent combines the evaluation scores.
7. Results Module presents the final evaluation.

## 5. Data Models

| Model | Important Fields |
|---|---|
| Evaluation Input | question, ai_response, reference_answer, reference_document |
| Retrieved Evidence | text, dataset, source_question, distance |
| Agent Result | agent_name, score, findings |
| Final Result | relevance_score, accuracy_score, hallucination_risk, completeness_score, overall_score, verdict, explanation |

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API |
| Pandas | Data processing |
| TruthfulQA and SQuAD | Reference datasets |
| Sentence Transformers | Embedding generation |
| ChromaDB | Vector storage and retrieval |
| Swagger UI | API testing |
| Git and GitHub | Version control |