class TrieNode:
    def __init__(self):
        self.children = dict()
        self.val = 0 

class Trie:
    def __init__(self, n):
        self.root = TrieNode()
        self.n = n
        
    def add(self, num):
        node = self.root 
        for shift in range(self.n, -1, -1): 
            val = (num>>shift)&1
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.val = num
        
    def delete(self, num):
        return self._delete(num, self.binary_encode(num), 0, self.root)
    
    def binary_encode(self, num):
        bits = []
        for shift in range(self.n, -1, -1): 
            bit = (num>>shift)&1
            bits.append(bit)
        return bits
    
    def _delete(self, num, encode, i, current):
        if i == self.n+1:
            if current.val != num:
                return False
            current.val = 0

            # if there is no children, then we could remove this tree node
            return len(current.children) == 0
        
        # get the next node from the encode array
        b = encode[i]
        if b not in current.children:
            return False
        next_node = current.children[b]

        # get the delete signal from the children result
        need_del = self._delete(num, encode, i+1, next_node)
        if need_del:
            del current.children[b]

            # if there is no children, then we could remove this tree node
            return len(current.children) == 0

        return False

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        # The max size of value is 2*20
        max_bit_len = 21
        node = Trie(max_bit_len)

        # Try to record the available num
        queue = collections.deque()

        res = 0
        for num in nums:
            # If the num is too small, it will not satisfy the Strong Pair Condition
            # then we remove it from queue
            while queue and abs(num - queue[0]) > min(num, queue[0]):
                old = queue.popleft()
                # Update the tree
                node.delete(old)
            
            # Update the tree and queue
            node.add(num)
            queue.append(num)
            
            cur = node.root
            # Try to find the max answer from the tree
            for shift in range(max_bit_len, -1, -1):
                bit = (num>>shift)&1
                cur = cur.children[1-bit] if 1-bit in cur.children else cur.children[bit]
            res = max(res, num ^ cur.val)
            
        return res
