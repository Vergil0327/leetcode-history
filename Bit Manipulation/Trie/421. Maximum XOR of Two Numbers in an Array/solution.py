VAL = '@val'
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        XorTree = lambda: defaultdict(XorTree)

        tree = XorTree()
        def queryMaxXor(node, num):
            for i in range(32-1, -1, -1):
                b = (num>>i)&1
                target = 1-b
                if target in node:
                    node = node[target]
                elif b in node:
                    node = node[b]
                else:
                    return -1
            return num^node[VAL]
                    
        res = 0
        for num in nums:            
            res = max(res, queryMaxXor(tree, num))

            # add num to XOR tree
            node = tree
            for i in range(32-1, -1, -1):
                bit = (num>>i)&1
                if bit not in node:
                    node[bit] = XorTree()
                node = node[bit]
            node[VAL] = num
        return res