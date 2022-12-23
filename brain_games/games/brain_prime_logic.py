import math


def is_prime(num):
    num = abs(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    if abs(num) in [0, 1]:
        return False
    else:
        return True


def prime_logic(num):
    question = f'{num}'
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
