# https://leetcode.cn/problems/minimum-operations-to-equalize-subarrays/solutions/3845357/zhong-wei-shu-tan-xin-ke-chi-jiu-hua-xia-etpv/
# https://www.bilibili.com/video/BV1D4SiB5Ee3/?spm_id_from=333.1387.homepage.video_card.click
# persistent segment tree的概念像是 prefix sum + segment tree
# 如果我們能高效求出prefix segment tree (長度n+1), 那麼每個`l, r = queries[i]`都能透過prefix_segment_tree[r+1] - prefix_segment_tree[l]來得到[l, r]區間的segment tree
# 然後再利用這個segment tree去求出我們要的資訊

class Node:
    __slots__ = 'l', 'r', 'left', 'right', 'cnt', 'sum'

    def __init__(self, l: int, r: int, left=None, right=None, cnt=0, sum=0):
        self.l = l
        self.r = r
        self.left = left
        self.right = right
        self.cnt = cnt
        self.sum = sum

    def maintain(self):
        self.cnt = self.left.cnt + self.right.cnt
        self.sum = self.left.sum + self.right.sum

    @staticmethod
    def build(l: int, r: int) -> 'Node':
        node = Node(l, r)
        if l == r:
            return node
        mid = (l + r) // 2
        node.left = Node.build(l, mid)
        node.right = Node.build(mid + 1, r)
        return node

    # add val to node-i position in segment tree
    def add(self, i: int, val: int) -> 'Node':
        # copy current node information
        node = Node(self.l, self.r, self.left, self.right, self.cnt, self.sum)
        if node.l == node.r:
            node.cnt += 1
            node.sum += val
            return node
        mid = (node.l + node.r) // 2
        if i <= mid:
            node.left = node.left.add(i, val)
        else:
            node.right = node.right.add(i, val)
        node.maintain()
        return node

    # 查询 old 和 self 对应子数组的第 k 小，k 从 1 开始
    def kth(self, old: 'Node', k: int) -> int:
        if self.l == self.r:
            return self.l
        cnt_l = self.left.cnt - old.left.cnt
        if k <= cnt_l:  # 答案在左子树中
            return self.left.kth(old.left, k)
        return self.right.kth(old.right, k - cnt_l)  # 答案在右子树中

    # 查询 old 和 self 对应子数组，有多少个数 <= i，这些数的元素和是多少
    def query(self, old: 'Node', i: int) -> Tuple[int, int]:
        if self.r <= i:
            return self.cnt - old.cnt, self.sum - old.sum
        cnt, sum_ = self.left.query(old.left, i)
        mid = (self.l + self.r) // 2
        if i > mid:
            c, s = self.right.query(old.right, i)
            cnt += c
            sum_ += s
        return cnt, sum_


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        leftmost = [0] * n
        for i in range(1, n):
            leftmost[i] = leftmost[i - 1] if nums[i] % k == nums[i - 1] % k else i

        # 離散化, nums[i] <= 10^9 壓縮到 nums.length範圍內
        sorted_nums = sorted(set(nums))
        mp = {x: i for i, x in enumerate(sorted_nums)}

        # construct persistent segment tree
        t = [None] * (n + 1)
        t[0] = Node.build(0, len(sorted_nums) - 1)
        for i, x in enumerate(nums):
            j = mp[x]  # 離散化
            t[i + 1] = t[i].add(j, x)

        ans = []
        for l, r in queries:
            if leftmost[r] > l:  # 無解
                ans.append(-1)
                continue

            r += 1  # 改成左閉右開，利於計算

            # 計算區間中位數
            sz = r - l
            i = t[r].kth(t[l], sz // 2 + 1)
            median = sorted_nums[i]  # 離散化後的值 -> 原始值

            # 計算區間所有元素到中位數的距離和, 中位數位置會是最小操作數的目標
            total = t[r].sum - t[l].sum  # 區間元素和
            cnt_left, sum_left = t[r].query(t[l], i)
            s = median * cnt_left - sum_left  # 小於等於中位數位置所需操作數
            s += total - sum_left - median * (sz - cnt_left)  # 大於中位數位置所需操作數
            ans.append(s // k)  # 操作次數 = 總距離 / k

        return ans
