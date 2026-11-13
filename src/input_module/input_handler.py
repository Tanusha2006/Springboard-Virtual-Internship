
def validate_evaluation_input(
    question,
    ai_response,
    reference_answer="",
    reference_document=""
):
    question = question.strip()
    ai_response = ai_response.strip()
    reference_answer = reference_answer.strip()
    reference_document = reference_document.strip()

    if not question:
        raise ValueError("Question cannot be empty.")

    if not ai_response:
        raise ValueError("AI response cannot be empty.")

    evaluation_input = {
        "question": question,
        "ai_response": ai_response,
        "reference_answer": reference_answer or None,
        "reference_document": reference_document or None
    }

    return evaluation_input
