import prompt 

from brain_games.cli import welcome_user
from brain_games.games.even import DESCRIPTION, get_round


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(DESCRIPTION)

    attempts = 3
    for _ in range(attempts):
        question, correct_answer = get_round()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer." f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()