# Evaluation Methodology

## 1. Overview

The system checks AI-generated answers based on relevance, accuracy, hallucinations and completeness. Each factor is evaluated separately using the available reference information.

## 2. Evaluation Factors

- **Relevance:** Checks whether the answer is related to the question.
- **Accuracy:** Checks whether the given facts are correct.
- **Hallucination:** Finds information that is unsupported or contradicts the reference.
- **Completeness:** Checks whether any important information is missing.

## 3. Scoring

Each factor will be given a score from 0 to 5.

| Score | Meaning |
|---|---|
| 0–1 | Poor |
| 2 | Below average |
| 3 | Acceptable |
| 4 | Good |
| 5 | Excellent |

For hallucination risk, the scoring is reversed: 0 means no detected risk, while 5 means very high risk.

## 4. Final Verdict

Based on the evaluation results, the system will provide one of the following:

- **Reliable:** The answer is well-supported by the available evidence.
- **Needs Review:** Some parts of the answer need further checking.
- **Unreliable:** Major errors or unsupported claims are found.
- **Insufficient Evidence:** There is not enough information to judge the answer.

## 5. Evaluation Process

1. Receive the question and AI-generated answer.
2. Search for relevant reference information.
3. Evaluate the answer using the four factors.
4. Collect the scores and identified issues.
5. Generate the final verdict.
6. Display the results with supporting evidence.

## 6. Expected Output

The system will generate a report showing the scores, detected issues, supporting information and final verdict.
