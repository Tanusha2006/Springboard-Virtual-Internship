
from fastapi import FastAPI

app = FastAPI(
    title="AI Response Validation System",
    description="Backend API for collecting evaluation inputs"
)

@app.post("/evaluate")
def evaluate_response(data: dict):

    question = data.get("question", "").strip()
    ai_response = data.get("ai_response", "").strip()
    reference_answer = data.get("reference_answer", "").strip()

    if not question:
        return {"error": "Question cannot be empty"}

    if not ai_response:
        return {"error": "AI response cannot be empty"}

    return {
        "message": "Input received successfully",
        "question": question,
        "ai_response": ai_response,
        "reference_answer": reference_answer or None
    }
