import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_round():
    max_gcd = random.randint(1, 100)
    min_gcd = random.randint(1, 100)
    result = gcd(max_gcd, min_gcd)
    question = f"{max_gcd} {min_gcd}"
    correct_answer = str(result)

    return question, correct_answer