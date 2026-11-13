
from fastapi import FastAPI, HTTPException
from input_handler import validate_evaluation_input
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE_DIR / "src" / "data_processing"))

from retrieval import retrieve_reference_context

app = FastAPI(
    title="AI Response Validation System",
    description="Backend API for collecting and retrieving evaluation inputs"
)


@app.post("/evaluate")
def evaluate_response(data: dict):
    try:
        evaluation_input = validate_evaluation_input(
            question=data.get("question", ""),
            ai_response=data.get("ai_response", ""),
            reference_answer=data.get("reference_answer", ""),
            reference_document=data.get("reference_document", "")
        )

        reference_context = retrieve_reference_context(
            evaluation_input["question"]
        )

        return {
            "message": "Input received and reference context retrieved successfully",
            "evaluation_input": evaluation_input,
            "retrieved_context": reference_context
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Evaluation processing failed: {str(error)}"
        )
