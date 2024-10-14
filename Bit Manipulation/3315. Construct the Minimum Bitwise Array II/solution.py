class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if num%2 == 0:
                res.append(-1)
            else:
                t = num
                x = 0
                while t:
                    if (t+1).bit_count() == 1: # 二進制為連續的1000..000, 代表t為連續的111...111
                        x += t>>1
                        break
                    else:
                        m = t.bit_length()-1

                        x += 1<<m
                        t -= 1<<m
                
                res.append(x)
                
        return res
