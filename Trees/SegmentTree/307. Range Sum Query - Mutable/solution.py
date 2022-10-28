
# recursive solution: https://www.youtube.com/watch?v=3faZ-iTte7k
class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.n = N
        self.seg = [0] * (2*N)
        
        # insert leaf nodes
        for i in range(N):
            self.seg[N+i] = nums[i]
        
        # construct segment tree
        for i in range(N-1, -1, -1):
            # seg.tree[i] = seg.tree[2*i] + seg.tree[2*i+1]
            self.seg[i] = self.seg[i<<1] + self.seg[i<<1|1]

    def update(self, index: int, val: int) -> None:
        index += self.n
        # update value at leaf
        self.seg[index] = val
        
        # update upward
        while index > 1:
            self.seg[index>>1] = self.seg[index] + self.seg[index^1]
            index >>= 1

    def sumRange(self, left: int, right: int) -> int:
        # segment tree is [l, r)
        total = 0
        l, r = left+self.n, (right+1)+self.n
        while l < r:
            if l&1:
                total += self.seg[l]
                l += 1
            if r&1:
                r-=1
                total += self.seg[r]
            l, r = l>>1, r>>1
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)