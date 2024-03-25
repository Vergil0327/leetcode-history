class TrieNode:
    def __init__(self):
        self.next = dict()
        self.val = 0

class Trie:
    def __init__(self, n):
        self.n = n
        self.root = TrieNode()

    def add(self, num):
        node = self.root
        for i in range(self.n, -1, -1):
            val = (num>>i)&1
            if val not in node.next:
                node.next[val] = TrieNode()
            
            node = node.next[val]
        node.val = num

    def findMaxXOR(self, val):
        cur = self.root
        for i in range(self.n, -1, -1):
            bit = (val>>i)&1
            cur = cur.next[1-bit] if 1-bit in cur.next else cur.next[bit]
        return val^cur.val
    
    def delete(self, num):
        bits = []
        for i in range(self.n, -1, -1):
            bit = (num>>i)&1
            bits.append(bit)
        return self._delete(num, bits, 0, self.root)
    
    def _delete(self, num, encodes, i, current):
        if i == self.n+1:
            if current.val != num: return False
            current.val = 0
            return len(current.next) == 0
        
        b = encodes[i]
        if b not in current.next: return False

        next_node = current.next[b]

        need_del = self._delete(num, encodes, i+1, next_node)
        if need_del:
            del current.next[b]
            return len(current.next) == 0
        return False

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        root = -1
        for node, p in enumerate(parents):
            if p == -1:
                root = node
                continue
            graph[p].append(node)

        max_bit_length = ceil(log2(2 * 10**5)) # 0 <= queries[i].val <= 2 * 10^5
        tri = Trie(max_bit_length)

        res = [0]*len(queries)

        query2idx = defaultdict(set)
        for i, (node, val) in enumerate(queries):
            query2idx[node].add(i)

        def dfs(node):
            tri.add(node)
            if node in query2idx:
                for idx in query2idx[node]:
                    res[idx] = tri.findMaxXOR(queries[idx][1])

            for children in graph[node]:
                dfs(children)

            tri.delete(node)

        dfs(root)
        return res