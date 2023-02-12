# val ^ first == second
# val ^ first ^ first == second ^ first
# val == second ^ first

# Brute Force
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:        
        n = len(s)

        res = []
        for first, second in queries:
            target = second^first
            substr = str(bin(target))[2:]
            if substr not in s:
                res.append([-1, -1])
            else:
                # idx = s.find(substr)
                for i in range(n-len(substr)+1):
                    if s[i:i+len(substr)] == substr:
                        res.append([i, i+len(substr)-1])
                        break
        return res

# Hashing
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        preprocess = {}
        for i in range(n):
            # we don't want leading zeros in bits
            # but we still need to store position for bit `0`
            bit = 0
            if s[i] == "0":
                if bit not in preprocess:
                    preprocess[bit] = [i, i]
                continue

            for j in range(i, min(i+32, n)):
                bit = (bit<<1) | int(s[j])
                if bit not in preprocess:
                    preprocess[bit] = [i, j]
        
        res = []
        for first, second in queries:
            target = second^first
            if target in preprocess:
                res.append(preprocess[target])
            else:
                res.append([-1,-1])
        return res