import requests
import html
import random

def fetch_categories():
    """
    Fetches all available quiz categories from OpenTDB API.
    Returns a dict: {"Category Name": category_id}
    """
    url = "https://opentdb.com/api_category.php"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {item["name"]: item["id"] for item in data["trivia_categories"]}
    else:
        raise Exception("Failed to fetch categories from OpenTDB.")

def generate_quiz(topic=None, difficulty="medium"):
    """
    Fetches 5 relevant questions from OpenTDB API based on topic (category).
    """
    categories = fetch_categories()
    
    if topic not in categories:
        topic = "General Knowledge"  # fallback topic
    
    category_id = categories[topic]

    url = f"https://opentdb.com/api.php?amount=10&category={category_id}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    data = response.json()

    if data["response_code"] != 0 or not data["results"]:
        raise ValueError("Could not fetch questions from OpenTDB")

    all_questions = data["results"]
    selected_questions = random.sample(all_questions, min(5, len(all_questions)))

    formatted_quiz = []

    for item in selected_questions:
        options = item["incorrect_answers"] + [item["correct_answer"]]
        random.shuffle(options)

        explanation = explanation = f"""
The answer is: {html.unescape(item['correct_answer'])}

**Justification**  
The correct answer is '{html.unescape(item['correct_answer'])}' because it best addresses the core concept being tested. Here's why:

1. It accurately reflects the main function, role, or fact related to the topic.
2. It aligns with verified knowledge and widely accepted information.
3. It provides a clear and logical interpretation of the question's context.

**Other Options**  
Some of the other choices, such as '{html.unescape(item['incorrect_answers'][0])}', might seem plausible but are ultimately incorrect because:

- They either represent secondary or unrelated functions.
- They may contain misconceptions or incomplete information.
- They don't fully align with established facts or technical definitions.

**Conclusion**  
Considering the key facts and reasoning above, '{html.unescape(item['correct_answer'])}' is clearly the most accurate and appropriate choice, making it the correct answer.
"""



        formatted_quiz.append({
            "question": html.unescape(item["question"]),
            "options": [html.unescape(opt) for opt in options],
            "answer": html.unescape(item["correct_answer"]),
            "explanation": explanation
        })

    return formatted_quiz
