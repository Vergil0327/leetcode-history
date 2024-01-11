class TrieNode:
    def __init__(self):
        self.next = {}
        self.val = -1
class Trie:
    def __init__(self, n):
        self.root = TrieNode()

    def add(self, num):
        node = self.root
        for i in range(31, -1, -1):
            b = (num>>i)&1
            if b not in node.next:
                node.next[b] = TrieNode()
            node = node.next[b]
        node.val = num

    def find_max_xor(self, num):
        node = self.root
        for i in range(31, -1, -1):
            b = (num>>i)&1
            if 1-b in node.next:
                node = node.next[1-b]
            elif b in node.next:
                node = node.next[b]
            else:
                return -1
        return num^node.val

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)

        nums.sort()
        res = [-1] * m

        q = sorted([m, x, i] for i, (x, m) in enumerate(queries))
        root = Trie(32)
        j = 0
        for m, x, idx in q:
            while j < n and nums[j] <= m:
                root.add(nums[j])
                j += 1
            res[idx] = max(res[idx], root.find_max_xor(x))
        return res
