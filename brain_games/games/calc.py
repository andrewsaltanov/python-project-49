import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    op = random.choice(['+', '-', '*'])

    match op:
        case '+':
            correct = str(a + b)
        case '-':
            correct = str(a - b)
        case '*':
            correct = str(a * b)

    question = f"{a} {op} {b}"
    return question, correct