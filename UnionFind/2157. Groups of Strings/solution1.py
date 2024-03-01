class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        
        def encode(s):
            bit = 0
            for ch in s:
                bit |= (1<<(ord(ch)-ord("a")))
            return bit

        arr = []
        for word in words:
            arr.append(encode(word))

        # union-find
        parent = list(range(n))
        rank = [1]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        index = {}
        for i, bit in enumerate(arr):
            if bit in index:
                union(i, index[bit])
                index[bit] = find(i)
            else:
                index[bit] = i

        for i, bit in enumerate(arr):
            # replace
            for j in range(26):
                if (bit>>j)&1: # replace existed one
                    for k in range(26):
                        if (bit>>k)&1: continue

                        new_bit = bit
                        new_bit ^= (1<<j)
                        new_bit ^= (1<<k)
                        if new_bit in index:
                            union(i, index[new_bit])

            # delete
            for j in range(26):
                if (bit>>j)&1:
                    new_bit = bit^(1<<j)
                    if new_bit in index:
                        union(i, index[new_bit])

        groups = set()
        for i in parent:
            p = find(i)
            groups.add(p)

        return [len(groups), max(rank)]