




  
class RingQueue:
    def __init__(self, maxsize: int) -> None:
        self._queue = [None for i in range(maxsize)]
        self.maxsize = maxsize
        self.head = -1
        self.tail = -1

    def push(self, obj) -> None:
        assert ((self.tail + 1) % self.maxsize != self.head), 'очередь заполнена'

        if (self.head == -1):
            self.head = 0
            self.tail = 0
        
        else:
            self.tail = (self.tail + 1)%self.maxsize

        self._queue[self.tail] = obj

    def pop(self):
        assert self.head != -1, 'empty'
    
        if self.head == self.tail:
            self.head = self.tail = -1

        else:
            self.head = (self.head + 1)%self.maxsize

        data = self._queue[self.head]   
        return data

    def first(self):
        return self._queue[self.head]

    def size(self) -> int:
        return (self.maxsize)


    def __str__(self) -> str:
        return str(self._queue)    


queue = RingQueue(3)

queue.push(1)
queue.push(2)
queue.push(3)


print(queue)



