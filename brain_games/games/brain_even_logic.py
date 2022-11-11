def even_logic(num):
    question = f'{num}'
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
