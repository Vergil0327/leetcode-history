
"""
Example Usage

n = 100000
bit = Bit(n)

for i in range(1, n+1):
    bit.udpateDelta(i, nums[i])
    print(bit.queryPresum(i))
"""
class BIT:
    def __init__(self, n):
        self.n = n
        self.bitArr = [0] * (n+1) # 1-indexed arrays

    # increase nums[i] by delta
    def udpateDelta(self, i: int, delta: int):
        idx = i
        n = self.n
        arr = self.bitArr
        while idx <= n:
            arr[idx] += delta
            idx +=  idx & (-idx)

    # sum of range nums[1:i] inclusively
    def queryPresum(self, i: int) -> int:
        idx = i
        n = self.n
        arr = self.bitArr
        
        res = 0
        while idx <= n:
            res += arr[idx]
            # res %= mod # we can mod here if need it
            idx -= idx & (-idx)
        return res

    # sum of range nums[i:j] inclusively
    def sumRange(self, i: int, j: int) -> int:
        return self.queryPresum(j) - self.queryPresum(i-1)
