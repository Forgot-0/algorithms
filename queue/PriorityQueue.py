


class Node:
    def __init__(self, obj, next=None, prev=None, priority=None) -> None:
        self._obj = obj
        self.next = next
        self.prev = prev
        self.priority = priority

    def __str__(self) -> str:
        return f'{self._obj} <-> {self.next}'

    def __eq__(self, __value: object) -> bool:
        return self._obj == __value

    def __lt__(self, __value: object) -> bool:
        return self.priority < __value.priority

    def __le__(self, __value: object) -> bool:
        return self.priority <= __value.priority

    def __eq__(self, __value: object) -> bool:
        return self.priority == __value.priority


class PriorityQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.lenght = 0

    def add_back(self, obj) -> None:
        node = Node(obj, prev=self.tail)

        if self.tail:
            self.tail.next = node
            self.tail = node
            self.lenght += 1
        
        else:
            self.head = node
        self.tail = node
        self.lenght += 1

    def add_first(self, obj) -> None:
        node = Node(obj, self.head)
        if self.head:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node
        self.lenght += 1

    def pop(self) -> Node:
        assert self.lenght != 0, 'Очередь пуста'
        max_priority = self.head
        while max_priority.next:
            if max_priority < max_priority.next:
                max_priority = max_priority.next

        return max_priority

    def __str__(self) -> str:
        return str(self.head)


n = Node(2, priority=1)
n1 = Node(3, priority=2)

lst = PriorityQueue()

lst.add_first(1)
lst.add_first(2)

print(lst)