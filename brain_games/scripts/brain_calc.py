#! /usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.main_game_calc_prog_logic import main_game


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    main_game('calc', name)


if __name__ == '__main__':
    main()
