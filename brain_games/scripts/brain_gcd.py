#! /usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.main_game_logic import main_game


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    main_game('gcd', name)


if __name__ == '__main__':
    main()
