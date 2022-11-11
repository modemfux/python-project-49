import math


def is_prime(num):
    num == abs(num)
    if num == 0 or num == 1:
        return False
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    else:
        return True


def prime_logic(num):
    question = f'{num}'
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
