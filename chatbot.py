import json
from difflib import SequenceMatcher


# Load FAQ data
with open("faq.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)


def similarity(text1, text2):
    """Calculate similarity between two questions."""

    return SequenceMatcher(
        None,
        text1.lower(),
        text2.lower()
    ).ratio()


def get_response(user_question):
    """Find the best answer for the user's question."""

    best_score = 0
    best_answer = None

    for item in faq_data:

        score = similarity(
            user_question,
            item["question"]
        )

        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    # If question is not similar enough
    if best_score < 0.35:

        return (
            "Sorry, I don't understand your question. "
            "Please contact customer support."
        )

    return best_answer