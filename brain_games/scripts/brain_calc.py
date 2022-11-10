#! /usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.brain_calc import brain_calc

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    brain_calc(name)


if __name__ == '__main__':
    main()
