class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [(0, 0)] * (4 * size)
        self.lazy = [0] * (4 * size)
        self.build(1, 0, size - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = (0, 0)
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.pull(node)

    def pull(self, node):
        self.tree[node] = (
            min(self.tree[2 * node][0], self.tree[2 * node + 1][0]),
            max(self.tree[2 * node][1], self.tree[2 * node + 1][1])
        )

    def push(self, node):
        if self.lazy[node] != 0:
            self.tree[2 * node] = (self.tree[2 * node][0] + self.lazy[node],
                                   self.tree[2 * node][1] + self.lazy[node])
            self.tree[2 * node + 1] = (self.tree[2 * node + 1][0] +
                                       self.lazy[node], self.tree[2 * node + 1][1] + self.lazy[node])
            self.lazy[2 * node] += self.lazy[node]
            self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if start > end or start > r or end < l:
            return
        if l <= start and end <= r:
            self.tree[node] = (self.tree[node][0] + val,
                               self.tree[node][1] + val)
            self.lazy[node] += val
            return

        self.push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        self.pull(node)

    def update_range(self, l, r, val):
        self.update(1, 0, self.size - 1, l, r, val)

    def f_left(self, node, start, end, l, r, target):
        if start > end or start > r or end < l:
            return float('inf')
        if self.tree[node][0] > target or self.tree[node][1] < target:
            return float('inf')
        if start == end:
            return start if self.tree[node][0] == target else float('inf')

        self.push(node)
        mid = (start + end) // 2

        lft = self.f_left(2 * node, start, mid, l, r, target)
        if lft != float('inf'):
            return lft
        return self.f_left(2 * node + 1, mid + 1, end, l, r, target)

    def min_left(self, l, r, target):
        return self.f_left(1, 0, self.size - 1, l, r, target)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        last = {}
        pre = [-1] * n # the current occurrence of nums[i] is responsible for the range [pre[i]+1, i]
        for i in range(n):
            if nums[i] in last:
                pre[i] = last[nums[i]]
            last[nums[i]] = i

        st = SegmentTree(n)
        
        res = 0
        for j in range(n):
            chg = 1 if nums[j] % 2 == 0 else -1 # 1 or -1

            # Adds +1 (or -1) to all positions in range [pre[j]+1, j]
            # This marks: "if your subarray starts anywhere in [pre[j]+1, j] and ends at j, you now have one more distinct value of nums[j]"
            st.update_range(pre[j]+1, j, chg)

            i = st.min_left(0, j, 0)
            if i != float('inf'):
                res = max(res, j - i + 1)

        return res