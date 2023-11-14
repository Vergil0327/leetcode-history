class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefix = 0
        seen = Counter() # bitmask: count
        seen[0] = 1
        res = 0
        for ch in word:
            bit = 1<<(ord(ch)-ord("a"))
            prefix ^= bit

            # 0 odd character substr
            res += seen[prefix]
            
            # iterate a-j and check if there is at most 1 a-j in substr
            for i in range(10):
                premask = prefix^(1<<i)
                res += seen[prefix^(1<<i)]
                

            seen[prefix] += 1
        return res
