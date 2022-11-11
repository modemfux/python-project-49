import random


def math_operations(num1, num2, operator):
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        return (question, num1 + num2)
    elif operator == '-':
        return (question, num1 - num2)
    elif operator == '*':
        return (question, num1 * num2)
    elif operator == '/':
        return (question, num1 / num2)


def calc_logic(num1, num2, operator):
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        return (question, str(num1 + num2))
    elif operator == '-':
        return (question, str(num1 - num2))
    elif operator == '*':
        return (question, str(num1 * num2))
    elif operator == '/':
        return (question, str(num1 / num2))


def brain_calc(name):
    print('What is the result of the expression?')
    operators = ['+', '-', '*']
    i = 0
    while i < 3:
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        operator = random.choice(operators)
        equation, correct_answer = math_operations(rand_num1, rand_num2, operator)
        print(f'Question: {equation}')
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')
