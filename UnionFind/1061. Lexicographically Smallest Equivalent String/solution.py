# # reflexivity
# a: [a]
# b: [b]

# # symmetry
# a: [a, b]
# b: [b, a]

# # transitivity
# a: [a, b, c]
# b: [b, a]
# Union-Find
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)] # each english letter's parent

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb: return
            if pa < pb: # union to Lexicographically smaller one
                parent[pb] = pa
            else:
                parent[pa] = pb
        
        for a, b in zip(s1, s2):
            union(ord(a)-ord("a"), ord(b)-ord("a"))

        res = ""
        for c in baseStr:
            res += chr(ord("a")+find(ord(c)-ord("a")))
        return res