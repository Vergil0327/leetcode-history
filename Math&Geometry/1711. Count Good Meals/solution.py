class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10**9 + 7
        
        count = Counter(deliciousness)
        keys = list(sorted(count.keys()))
        n = len(keys)

        res = 0
        for p in range(22):
            target = pow(2, p)
            
            j = n-1
            for i in range(n):
                while j > i and keys[i] + keys[j] > target:
                    j -= 1
                if j < i: break
                if keys[i] + keys[j] == target:
                    if i == j:
                        res += comb(count[keys[i]], 2)
                    else:
                        res += count[keys[i]] * count[keys[j]]
                    res %= mod
        return res