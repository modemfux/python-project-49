#! /usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.main_game_logic import main_game


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    main_game('prime', name)


if __name__ == '__main__':
    main()
