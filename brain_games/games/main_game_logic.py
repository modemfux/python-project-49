import random
from brain_games.games.brain_calc_logic import calc_logic
from brain_games.games.brain_even_logic import even_logic
from brain_games.games.brain_gcd_logic import gcd_logic
from brain_games.games.brain_progression_logic import progression_logic
from brain_games.games.brain_prime_logic import prime_logic


def main_game(game, name):
    i = 0
    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        if game == 'calc':
            game_question, correct_answer = calc_logic(num1, num2, operator)
        elif game == 'even':
            game_question, correct_answer = even_logic(num1)
        elif game == 'gcd':
            game_question, correct_answer = gcd_logic(num1, num2)
        elif game == 'progression':
            length = random.randint(5, 15)
            game_question, correct_answer = progression_logic(num1, num2, length)
        elif game == 'prime':
            game_question, correct_answer = prime_logic(num1)
        print(f'Question: {game_question}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')
