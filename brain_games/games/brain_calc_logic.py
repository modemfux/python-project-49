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
