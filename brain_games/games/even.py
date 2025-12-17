import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    question = random.randint(1, 100) # NOSONAR
    correct_answer = "yes" if question % 2 == 0 else "no"
    return question, correct_answer