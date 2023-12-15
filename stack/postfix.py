import re
from main import Stack

PRIORITY = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

OPERATIONS = ['+', '-', '*', '/', '(', ')']


def infix_to_postfix(stroka: str) -> list:
    answer = []
    operations = Stack()

    stroka = re.split("([^0-9])", stroka)

    for token in stroka:
        if token == '' or token == ' ':
            continue

        if token not in OPERATIONS:
            answer += [int(token)]

        else:

            if token == ')':
                while operations.len() and operations.next() != '(':
                    answer += operations.pop()
                operations.pop()

            elif token == '(':
                operations.push(token)

            else:
                while (operations.len() and operations.next() != '(' 
                       and PRIORITY[token] <= PRIORITY[operations.next()]):
                    answer += operations.pop()
                operations.push(token)

    while operations.len():
        answer += operations.pop()

    return answer

def execute(oper: str, num1: int, num2: int) -> int:
    d = {
        '+': lambda x, y:  x + y,
        '-': lambda x, y:  x - y,
        '*': lambda x, y:  x * y,
        '/': lambda x, y:  x / y,
    }
    return d[oper](num1, num2)

def calc(lst: list) -> int:

    numbers = Stack()

    for token in lst:
        if token not in OPERATIONS:
            numbers.push(int(token))

        else:
            n2 = numbers.pop()
            n1 = numbers.pop()
            if token == '/' and n2 == 0:
                raise ZeroDivisionError
            numbers.push(execute(token, n1, n2))

    return numbers.pop()




res = (infix_to_postfix('1+(2*2 - 3)'))
# res = (infix_to_postfix('(+ 2 4)'))


print(res)
print(calc(res))