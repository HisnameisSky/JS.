import random

questions = [
    {
        "category": "Science",
        "question": "What is the chemical symbol for Gold?",
        "choices": ["Au", "Ag", "Fe"],
        "answer": "Au",
    },
    {
        "category": "Geography",
        "question": "What is the capital of Japan?",
        "choices": ["Tokyo", "Kyoto", "Osaka"],
        "answer": "Tokyo",
    },
    {
        "category": "Math",
        "question": "What is 2 + 2?",
        "choices": ["3", "4", "5"],
        "answer": "4",
    },
    {
        "category": "Technology",
        "question": "Which programming language is known as the language of the web?",
        "choices": ["Python", "JavaScript", "C++"],
        "answer": "JavaScript",
    },
    {
        "category": "Gaming",
        "question": "Who is Mario's brother?",
        "choices": ["Luigi", "Wario", "Toad"],
        "answer": "Luigi",
    },
]


def get_random_question(questions_list):
    return random.choice(questions_list)


def get_random_computer_choice(choices_list):
    return random.choice(choices_list)


def get_results(question_obj, computer_choice):
    if computer_choice == question_obj["answer"]:
        return "The computer's choice is correct!"
    else:
        return f"The computer's choice is wrong. The correct answer is: {question_obj['answer']}"