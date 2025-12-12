import prompt


def start_game(description, generate_round):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(description)
    rounds = 3

    for _ in range(rounds):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip().lower()

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")