class ProductOfNumbers:

    def __init__(self):
        self.nums = defaultdict(list)
        self.i = 0
        

    def add(self, num: int) -> None:
        self.nums[num].append(self.i)
        self.i += 1 

    def getProduct(self, k: int) -> int:
        res = 1
        for num in range(101):
            j = bisect_left(self.nums[num], self.i-k)
            res *= pow(num, len(self.nums[num])-j)
        return res
