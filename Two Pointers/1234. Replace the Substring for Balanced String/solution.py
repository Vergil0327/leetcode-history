class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        required = n//4

        counter = Counter(s)
        if counter["Q"] == required and counter["W"] == required and counter["E"] == required and counter["R"] == required:
            return 0

        l = r = 0
        res = n
        while r < n:
            counter[s[r]] -= 1
            r += 1

            while l < r and (counter["Q"] <= required and counter["W"] <= required and counter["E"] <= required and counter["R"] <= required):
                res = min(res, r-l)
                counter[s[l]] += 1
                l += 1
            
        return res
        
        # QWER
        # 3131
        # 2131
        # 1021
        # QQWERQEE, expected: 2
        #  l
        #     r