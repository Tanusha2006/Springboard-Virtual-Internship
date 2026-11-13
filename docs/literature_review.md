# Literature Review

## 1. Introduction

Large Language Models (LLMs) are widely used to generate answers and explain information. However, their responses may sometimes contain incorrect facts, unsupported statements or incomplete information. Several research studies and tools have explored ways to identify these issues and improve the reliability of AI generated responses.

## 2. LLM Evaluation and Hallucination Detection

LLM evaluation involves checking the quality of generated responses based on factors such as accuracy, relevance and completeness.

Hallucination detection focuses on identifying information that is incorrect or not supported by available evidence. Some common approaches include comparing answers with reference information, retrieving relevant documents and checking individual factual statements.

## 3. Retrieval Augmented Generation (RAG)

RAG combines information retrieval with language model processing. It retrieves relevant information from external sources instead of depending only on the model's existing knowledge.

The process generally involves document collection, chunking, embedding generation, vector storage and semantic retrieval. This approach can help provide reference information for evaluating AI generated responses.

## 4. Existing Evaluation Frameworks

**RAGAS:** A framework used to evaluate RAG systems. It includes metrics such as faithfulness, answer relevance, context precision and context recall.

**TruLens:** A framework used to evaluate and monitor AI applications. It provides methods to examine groundedness, context relevance and answer relevance.

**LLM:** An approach in which a language model evaluates another model's response using predefined criteria. However, its results may be affected by biases and inconsistent judgements.

## 5. Public Datasets

**TruthfulQA:** A benchmark containing 817 questions designed to test whether language models provide truthful answers instead of repeating common misconceptions.

**SQuAD:** A question-answering dataset based on Wikipedia passages. SQuAD 2.0 also includes questions that cannot be answered using the given passage, making it useful for studying insufficient evidence detection.

Both datasets can be explored for testing and evaluating the proposed system.

## 6. Observations

The study of existing approaches highlights a few important points:

- A single overall score may not clearly identify individual errors.
- Reference information is important for checking factual reliability.
- Irrelevant or incomplete retrieved information can affect evaluation.
- Automated evaluation may produce incorrect judgements.
- Insufficient evidence should be treated differently from a confirmed false statement.

These observations will help guide the design and development of the proposed system.

## 7. References

Lin, S., Hilton, J., and Evans, O. (2022). TruthfulQA: Measuring How Models Mimic Human Falsehoods. Association for Computational Linguistics.
https://aclanthology.org/2022.acl-long.229/

Rajpurkar, P., Jia, R., and Liang, P. (2018). Know What You Don't Know: Unanswerable Questions for SQuAD. Association for Computational Linguistics.
https://aclanthology.org/P18-2124/

Es, S., James, J., Espinosa-Anke, L., and Schockaert, S. (2023). RAGAS: Automated Evaluation of Retrieval Augmented Generation.
https://arxiv.org/abs/2309.15217

Zheng, L. et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.
https://arxiv.org/abs/2306.05685

Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
https://arxiv.org/abs/2005.11401

TruLens Documentation. RAG Evaluation and Feedback Functions.
https://www.trulens.org/reference/trulens/feedback/templates/rag/
