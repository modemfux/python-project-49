import random
from brain_games.games.brain_calc_logic import calc_logic
from brain_games.games.brain_even_logic import even_logic



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
#        elif game == 'gcd':
#            game_question, correct_answer = gcd_logic(num1, num2)
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
