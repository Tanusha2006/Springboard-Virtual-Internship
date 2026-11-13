
from fastapi import FastAPI, HTTPException
from input_handler import validate_evaluation_input

app = FastAPI(
    title="AI Response Validation System",
    description="Backend API for collecting evaluation inputs"
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

        return {
            "message": "Input received successfully",
            "evaluation_input": evaluation_input
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
