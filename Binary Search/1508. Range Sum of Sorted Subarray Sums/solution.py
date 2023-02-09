# Brute Force: O(n^2)
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = int(1e9+7)
        arr = []

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1]+nums[i-1]
            arr.append(presum[i])
        for i in range(1, n):
            for j in range(i+1, n+1):
                arr.append(presum[j]-presum[i])

        arr.sort()
        total = 0
        for i in range(left-1, right):
            total = (total+arr[i])%MOD
        return total
    

# Binary Search
class Solution_TLE:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = int(1e9+7)

        # [1,2,3,4]
        #  l   r
        # [1,2,3,4]
        #    l   r
        # [1,2,3,4]
        #      l r
        # targetSum = 5
        # 1
        # 1+2
        # cnt += (2-0)
        # 2
        # 2 + 3
        # cnt += (3-1)
        # 3
        # cnt += (3-2)
        def smallerOrEqual(targetSum):
            cnt = currSum = r = 0
            for l in range(n):
                while r < n and currSum+nums[r] <= targetSum:
                    currSum += nums[r]
                    r += 1
                cnt += r-l
                currSum -= nums[l]

            return cnt

        totalSum = sum(nums)
        def kthSum(k):
            l, r = 1, totalSum
            while l < r:
                mid = l + (r-l)//2
                if smallerOrEqual(mid) < k: # how many ranges whose sum is smaller or equal to mid
                    l = mid+1
                else:
                    r = mid
            return l
        
        res = 0
        for k in range(left, right+1):
            res = (res + kthSum(k))%MOD
        return res