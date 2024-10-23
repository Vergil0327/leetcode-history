class FrontMiddleBackQueue:

    def __init__(self):
        self.left, self.right = deque(), deque()
        

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        if len(self.left) > len(self.right)+1:
            self.right.appendleft(self.left.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(self.left.pop())
            self.left.append(val)
        

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        if len(self.right) > len(self.left):
            self.left.append(self.right.popleft())
        

    def popFront(self) -> int:
        if not self.left: return -1

        res = self.left.popleft()
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())
        return res

    def popMiddle(self) -> int:
        if len(self.left) > len(self.right):
            return self.left.pop()
        else:
            if not self.left: return -1

            num = self.left.pop()
            if self.right:
                self.left.append(self.right.popleft())
            return num
    
    def popBack(self) -> int:
        if not self.right:
            return self.left.pop() if self.left else -1

        if len(self.left) > len(self.right):
            num = self.right.pop()
            self.right.appendleft(self.left.pop())
            return num
        else:
            return self.right.pop()