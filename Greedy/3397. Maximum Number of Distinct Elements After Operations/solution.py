class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        # res = [nums[0]-k]
        # for i in range(1, len(nums)):
        #     if res[-1] < nums[i]-k:
        #         res.append(nums[i]-k)
        #     elif res[-1]+1 <= nums[i]+k:
        #         res.append(res[-1]+1)
        
        # return len(res)

        # optimized, we only need current max distinct number
        cur_max = nums[0]-k
        distinct = 1
        for i in range(1, len(nums)):
            if cur_max < nums[i]-k:
                cur_max = nums[i]-k
                distinct += 1
            elif cur_max+1 <= nums[i]+k:
                cur_max = cur_max+1
                distinct += 1
        return distinct
