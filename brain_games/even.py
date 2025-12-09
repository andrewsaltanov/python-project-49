import random

DESCRIPTION = 'Answer "YES" if the number is even, otherwise answer "NO".'

def get_round():
    question = random.randint(1, 100)
    correct_answer = "yes" if question % 2 == 0 else "no"
    return question, correct_answer