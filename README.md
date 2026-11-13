# AI Response Validation System with Hallucination Detection Assistance

## About the Project

AI tools like ChatGPT and other Large Language Models (LLMs) can provide useful answers in seconds. However, not every answer they generate is necessarily correct. Sometimes, AI may provide incorrect facts or information that sounds convincing but has no proper supporting evidence. This is known as an AI hallucination.

This project focuses on developing a system that can check the quality and reliability of AI-generated responses and help identify such issues.

**Problem**

When we receive an answer from an AI tool, it can be difficult to know whether the information is actually correct, relevant and complete.

The aim of this project is to make that checking process easier by comparing AI-generated answers with relevant reference information and identifying possible mistakes or unsupported claims.

## Project Objectives

- Check whether an AI-generated response is relevant to the given question.
- Verify the factual accuracy of the information.
- Identify statements that may be incorrect or unsupported.
- Check whether the response covers the important parts of the question.
- Provide understandable evaluation results with supporting evidence wherever available.

## Plan to Build It

The system will take a question and an AI-generated response as input. Users can also provide a reference answer or source document if available.

The system will then retrieve relevant information from its reference knowledge base and evaluate the response using different evaluation modules.

The final result will include individual scores, possible errors, supporting evidence and an overall evaluation.

## Evaluation Areas

I plan to evaluate responses using four main dimensions:

1. **Relevance:** Does the answer actually address the question?
2. **Accuracy:** Is the information factually correct?
3. **Hallucination:** Does the answer contain fabricated or unsupported information?
4. **Completeness:** Does the answer cover the important information required?

## Planned Modules

- User Input Module
- Reference Knowledge Base
- Data Preprocessing and Chunking
- Embedding Generation
- Semantic Search and Retrieval
- Evaluation Agent Layer
- Scoring and Verdict Generation
- Results Dashboard

## Current Progress

We are currently working on Milestone 1, which focuses on understanding LLM evaluation techniques, studying hallucination detection methods, exploring RAG architecture and designing the initial system architecture.

The implementation will be developed and updated module by module.

## Technologies Under Consideration

Python, Streamlit, FastAPI, Hugging Face Datasets, Sentence Transformers, ChromaDB, RAGAS and TruLens.


## Project Information

- **Program:** Infosys Springboard Virtual Internship – Batch 5 (2026–27)
- **Project Title:** Development of AI Response Validation System with Hallucination Detection Assistance
- **Developer:** TANUSHA L
