import random


def brain_even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = random.randint(0, 100)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {random_number}')
        answer = input('Your answer: ')
        if (answer == 'yes' and random_number % 2 == 0) or (answer == 'no' and random_number % 2 == 1):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')


def even_logic(num):
    question = f'{num}'
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
