class Stack:
    def __init__(self) -> None:
        self._stack = []

    def push(self, obj):
        self._stack.append(obj)

    def pop(self):
        return self._stack.pop()

    def next(self):
        return self._stack[-1]

    def len(self):
        return len(self._stack)
    
    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def __str__(self) -> str:
        return str(self._stack)
