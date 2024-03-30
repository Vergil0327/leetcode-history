class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if reduce(lambda x, y:x|y, nums, 0) < k: return -1

        power = [pow(2, i) for i in range(32)]
            
        bits = [0]*32
        
        l = r = cur = 0
        res = n+1
        while r < n:
            for i in range(32):
                if (nums[r]>>i)&1:
                    bits[i] += 1
                    if bits[i] == 1:
                        cur += power[i]
            r += 1

            while l < r and cur >= k:
                res = min(res, r-l)

                for i in range(32):
                    if (nums[l]>>i)&1:
                        if bits[i] == 1:
                            cur -= power[i]
                        bits[i] -= 1
                l += 1

        return -1 if res == n+1 else res