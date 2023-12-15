PRIORITY = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '(': 2
}

OPERATIONS = ['+', '-', '*', '/', '(', ')']

def postfix(stroka: str) -> list:
    import re
    expression = re.split('([^0-9])', stroka)
    answers = []
    stack = []
    for token in expression:
        if token == '' or token == ' ':
            continue
        if token not in OPERATIONS:
            try:
                answers.append(int(token))
            except:
                return "WRONG"
        else:
            if token == ')':
                while len(stack) and stack[-1] != '(':
                    answers += stack.pop()
                stack.pop()
            elif token == '(':
                stack.append(token) 
            else:
                while (len(stack) and stack[-1] != '(' and PRIORITY[token] <= PRIORITY[stack[-1]]):
                    answers += stack.pop()
                stack.append(token)
    
    while len(stack):
        answers.append(stack.pop())

    return answers

def execute(oper: str, num1: int, num2: int):
    d = {
        '+': lambda x, y:  x + y,
        '-': lambda x, y:  x - y,
        '*': lambda x, y:  x * y,
        '/': lambda x, y:  x / y,
    }
    return d[oper](num1, num2)


def calc(postfix: list):
    numbers = []
    answrs = 0

    if postfix == 'WRONG':
        return 'WRONG'
    
    for token in postfix:
        if token not in OPERATIONS:
            numbers.append(token)
        else:
            n2 = numbers.pop()
            n1 = numbers.pop()
            if token == '/' and n2 == 0:
                raise ZeroDivisionError
            numbers.append(execute(token, n1, n2))
    
    if len(numbers) != 1:
        return 'WRONG'

    return numbers.pop()



print(calc(postfix('1+a+1')))