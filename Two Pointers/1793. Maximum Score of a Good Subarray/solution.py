# Concise
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = k
        res = minVal = nums[k]
        while l > 0 or r < n-1:
            left = nums[l-1] if l-1 >= 0 else -inf
            right  = nums[r+1] if r+1 < n else -inf
            if left > right:
                minVal = min(minVal, left)
                l -= 1
            else:
                minVal = min(minVal, right)
                r += 1
            res = max(res, minVal * (r-l+1))

        return res

# Optimized
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = k
        minVal = nums[k]
        res = nums[k]
        while l >= 0 and r < n:
            if l-1 >= 0 and r+1<n:
                left = min(minVal, nums[l-1])
                right = min(minVal, nums[r+1])
                if left > right:
                    l -= 1
                    minVal = min(minVal, nums[l])
                else:
                    r += 1
                    minVal = min(minVal, nums[r])
            elif l-1 >= 0:
                l -= 1
                minVal = min(minVal, nums[l])
            elif r+1 < n:
                r += 1
                minVal = min(minVal, nums[r])
            else:
                break
            res = max(res, minVal*(r-l+1))
        while l-1 >= 0:
            l -= 1
            minVal = min(minVal, nums[l])
            res = max(res, minVal*(r-l))
        while r+1 < n:
            r += 1
            minVal = min(minVal, nums[r])
            res = max(res, minVal*(r-l))
        return res

# 1st try
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = k
        window = [[nums[k], k]] # min heap
        res = nums[k]
        while l >= 0 and r < n:
            if l-1 >= 0 and r+1<n:
                left = min(window[0][0], nums[l-1])
                right = min(window[0][0], nums[r+1])
                if left > right:
                    l -= 1
                    heapq.heappush(window, [nums[l], l])
                else:
                    r += 1
                    heapq.heappush(window, [nums[r], r])
            elif l-1 >= 0:
                l -= 1
                heapq.heappush(window, [nums[l], l])
            elif r+1 < n:
                r += 1
                heapq.heappush(window, [nums[r], r])
            else:
                break
            res = max(res, window[0][0]*(r-l+1))
        while l-1 >= 0:
            l -= 1
            heapq.heappush(window, [nums[l-1], l])
            res = max(res, window[0][0]*(r-l))
        while r+1 < n:
            r += 1
            heapq.heappush(window, [nums[r+1], r])
            res = max(res, window[0][0]*(r-l))
        return res
