from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.gcd import DESCRIPTION, generate_round


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    start_game(name, DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()