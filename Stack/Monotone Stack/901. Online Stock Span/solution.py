class StockSpanner:

    def __init__(self):
        self.stack = [(float("inf"), 0)]

    # O(n), but amortized O(1): https://leetcode.com/problems/online-stock-span/discuss/168311/C%2B%2BJavaPython-O(1)
    def next(self, price: int) -> int:
        i = self.stack[-1][1]+1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        _, j = self.stack[-1]
        self.stack.append((price, i))

        return i-j


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
