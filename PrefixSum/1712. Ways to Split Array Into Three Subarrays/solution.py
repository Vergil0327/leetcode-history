class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7

        presum = [0]*(n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        res = 0
        for i in range(1, n-1):
            left = presum[i]
            l1, r1 = i+1, n
            while l1 < r1:
                mid = l1 + (r1-l1)//2
                if presum[mid]-presum[i] >= left:
                    r1 = mid
                else:
                    l1 = mid+1

            l2, r2 = i, n-1
            while l2 < r2:
                mid = r2 - (r2-l2)//2
                if presum[n]-presum[mid] >= presum[mid]-presum[i]:
                    l2 = mid
                else:
                    r2 = mid-1
            
            res += max(0, l2-l1+1)
            res %= mod
        return res

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        mod, l, r = 1000000007, 0, 0
        
        presum, res = list(accumulate(nums)), 0
        for i in range(n-2):
            # find left-most right_split
            if l <= i:
                l = i+1
            
            while l < n-1 and presum[l]-presum[i] < presum[i]: # mid >= left
                l += 1

            # find right-most right_split
            if r < l:
                r = l
            while r < n-1 and presum[n-1]-presum[r] >= presum[r]-presum[i]: # right >= mid
                r += 1
            res = (res + r-l)%mod
        return res