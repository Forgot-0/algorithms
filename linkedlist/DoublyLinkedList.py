

class Node:
    def __init__(self, obj, next=None, prev=None) -> None:
        self._obj = obj
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f'{self._obj} <-> {self.next}'
    
    def __eq__(self, __value: object) -> bool:
        return self._obj == __value


class DoublyLinkedList:
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


    def pop_front(self) -> Node:
        assert self.lenght != 0, 'Список пуст'
        if self.tail == self.head:
            self.tail = self.head = None
            return
        
        node = self.head
        self.head = self.head.next
        self.lenght -= 1
        
        return node
    
    def pop_back(self) -> Node:
        assert self.lenght != 0, 'Список пуст'
        if self.tail == self.head:
            self.tail = self.head = None
            return

        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.lenght -= 1
        return node



    def __str__(self) -> str:
        return str(self.head)



lst = DoublyLinkedList()

lst.add_first(1)
lst.add_back(2)

lst.add_first(1)


print(lst.pop_back())


print(lst)