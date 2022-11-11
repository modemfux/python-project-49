import random


def prog_logic(start, step, length):
    prog_list = []
    i = 0
    member = start
    while i < length:
        prog_list.append(str(member))
        member += step
        i += 1
    index = random.randint(0, length - 1)
    correct_answer = str(prog_list[index])
    prog_list[index] = '..'
    question = ' '.join(prog_list)
    return (question, correct_answer)
