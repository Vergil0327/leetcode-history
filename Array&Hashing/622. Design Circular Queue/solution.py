class MyCircularQueue:

    def __init__(self, k: int):
        self.size, self.capacity = 0, k
        self.buffer = [-1] * k
        self.ptr = 0


    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity: return False
        self.buffer[self.ptr] = value
        self.ptr = (self.ptr + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0: return False
        i = (self.ptr - self.size + self.capacity)%self.capacity
        self.buffer[i] = -1
        self.size -= 1
        return True
        

    def Front(self) -> int:
        i = (self.ptr - self.size + self.capacity)%self.capacity
        return self.buffer[i]

    def Rear(self) -> int:
        i = (self.ptr - 1 + self.capacity)%self.capacity
        return self.buffer[i]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
