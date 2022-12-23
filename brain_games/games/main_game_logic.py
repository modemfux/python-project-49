import random
from brain_games.games.brain_calc_logic import calc_logic
from brain_games.games.brain_progression_logic import prog_logic
from brain_games.games.brain_even_logic import even_logic
from brain_games.games.brain_gcd_logic import gcd_logic
from brain_games.games.brain_prime_logic import prime_logic


def main_game(game, name):
    i = 0
    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        length = random.randint(5, 15)
        games_dict = {
            'even': [even_logic, num1],
            'gcd': [gcd_logic, num1, num2],
            'prime': [prime_logic, num1],
            'calc': [calc_logic, num1, num2, operator],
            'progression': [prog_logic, num1, num2, length]
        }
        game_func = games_dict[game][0]
        game_question, correct_answer = game_func(*games_dict[game][1:])
        print(f'Question: {game_question}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            wrong1 = f"'{answer}' is wrong answer ;(."
            wrong2 = f"Correct answer was '{correct_answer}'."
            print(wrong1, wrong2)
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')