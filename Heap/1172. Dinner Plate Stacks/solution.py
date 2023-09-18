class DinnerPlates:

    def __init__(self, capacity: int):
        self.plate = []
        self.canPush = [] # min heap, [index]
        self.cap = capacity

    def push(self, val: int) -> None:
        plate = self.plate

        while self.canPush and self.canPush[0] < len(plate) and len(plate[self.canPush[0]]) == self.cap:
            heapq.heappop(self.canPush)

        if not self.canPush:
            heapq.heappush(self.canPush, len(plate))

        if self.canPush[0] == len(plate):
            plate.append([])
        
        plate[self.canPush[0]].append(val)

    def pop(self) -> int:
        plate = self.plate
        while plate and not plate[-1]:
            plate.pop()
        
        return self.popAtStack(len(plate) - 1)

    def popAtStack(self, index: int) -> int:
        plate = self.plate
        if index < 0 or index >= len(plate) or not plate[index]: return -1
        
        heapq.heappush(self.canPush, index)
        return plate[index].pop()
