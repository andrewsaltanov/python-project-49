import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_round():
    max_gcd = random.randint(1, 100)
    min_gcd = random.randint(1, 100)
    correct_answer = gcd(max_gcd, min_gcd)
    question = f"{max_gcd} {min_gcd}"

    return question, correct_answer