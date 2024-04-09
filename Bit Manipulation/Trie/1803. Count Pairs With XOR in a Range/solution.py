class TrieNode:
    def __init__(self):
        self.next = {}
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num):
        node = self.root
        
        for i in range(31, -1, -1):
            b = (num>>i)&1
            if b not in node.next:
                node.next[b] = TrieNode()
            node = node.next[b]
            node.cnt += 1
        

    def count(self, num, threshold):
        root = self.root
        res = 0
        for i in range(31, -1, -1):
            x = (num>>i)&1
            t = (threshold>>i)&1

            if t == 1:
                if x == 1:
                    # 1 XOR y ? 1 = threshold
                    if 1 in root.next:
                        res += root.next[1].cnt # y = 1

                    if 0 in root.next:
                        root = root.next[0] # y = 0
                    else:
                        break
                if x == 0:
                    # 0 XOR y ? 1 = threshold
                    # y=0 -> 0 XOR 0 < 1 = threshold
                    if 0 in root.next:
                        res += root.next[0].cnt

                    # y=1 -> 0 XOR 1 = 1 = threshold => 繼續遞歸看下個bit位
                    if 1 in root.next:
                        root = root.next[1]
                    else:
                        break
            else:
                if x == 1:
                    # 1 XOR y ? 0=threshold
                    # y = 0 -> 1 XOR 0 = 1 > 0 threshold => 此路找不到合法nums[j]

                    # y = 1 -> 1 XOR 1 = 0 == 0 threshold => 繼續看下個bit
                    if 1 in root.next:
                        root = root.next[1]
                    else:
                        break
                if x == 0:
                    # 0 XOR y ? 0=threshold
                    # y = 0 -> 0 XOR 0 = 0 == 0 threshold => 繼續遞歸看下個bit
                    if 0 in root.next:
                        root = root.next[0]
                    else:
                        break
                    # y = 1 -> 0 XOR 1 = 1 > 0 threshold => 此後找出的nums[j]都無法使得nums[i]^nums[j] <= threshold
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        n = len(nums)

        res = 0
        root = Trie()
        for i in range(n):
            hi = root.count(nums[i], high+1)
            lo = root.count(nums[i], low)
            res += hi-lo
            root.add(nums[i])
        return res
