# Evaluation Input Module Implementation

## 1. Overview

The Evaluation Input Module collects the information required to evaluate an AI-generated response. It accepts a user question, AI response and optional reference information.

## 2. Implemented Features

- Accepts user questions.
- Accepts AI-generated responses.
- Supports an optional reference answer.
- Supports optional reference document text.
- Validates required inputs.
- Handles empty or missing reference information.
- Provides a FastAPI endpoint to receive evaluation requests.

## 3. Technologies Used

- Python
- FastAPI
- Uvicorn
- Requests

## 4. Testing

The API was tested using FastAPI TestClient in Google Colab.

The following cases were checked:

1. Valid question and AI response – successful.
2. Empty question – rejected.
3. Empty AI response – rejected.
4. Missing reference answer – accepted.
5. Missing reference document – accepted.

## 5. Current Status

The basic input handling, validation and backend API integration have been implemented and tested.

Actual document uploading, PDF/text extraction and user interface integration are still pending.
