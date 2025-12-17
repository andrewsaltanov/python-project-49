import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, length=10):
    progression = []
    current = start
    for _ in range(length):
        progression.append(current)
        current += step
    return progression


def generate_round():
    length = random.randint(5, 10)  # NOSONAR
    start = random.randint(1, 10)  # NOSONAR
    step = random.randint(0, 20)  # NOSONAR

    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)  # NOSONAR
    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer