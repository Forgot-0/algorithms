

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f'{self.value} -> {self.next}'
    
    def __eq__(self, __value: object) -> bool:
        return self.value == __value


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.lenght = 0

    def add_back(self, obj) -> None:
        node = Node(obj)

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

        if not self.tail:
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

        node = self.head
        while node.next != self.tail:
            node = node.next
        
        node.next = None
        node, self.tail = self.tail, node

        self.lenght -= 1

        return node


    def isPalindrome(self) -> bool:
        slow, fast, prev = self.head, self.head, None

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, slow, prev.next = slow, slow.next, None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        fast, slow = self.head, prev

        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next

        return True
    
    def reverseList(self):
        prev = None
    
        node = self.head

        while node:
            next = node.next
            node.next = prev

            prev = node
            node = next
            
        return prev      

    def find(self, el) -> bool:
        node = self.head
        while node.next != self.tail:
            if node.value == el:
                return True
            node = node.next
        return False
    


    def __str__(self) -> str:
        return str(self.head)




lst = LinkedList()
lst.add_back(2)
lst.add_back(3)

lst.add_first(4)
print(lst.pop_back())
print(lst)