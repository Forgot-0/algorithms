def isValid(self, s: str) -> bool:
    order = []

    for i in s:
        if i in "([{":
            order.append(i)

        elif len(order) <= 0 or '([{'[")]}".index(i)] != order.pop():
            return False

    return len(order) == 0