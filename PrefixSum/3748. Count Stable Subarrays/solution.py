class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        valid_interval = [[]]
        for i in range(n):
            if not valid_interval[-1]:
                valid_interval[-1].append(i)
            elif nums[i] >= nums[valid_interval[-1][-1]]:
                valid_interval[-1].append(i)
            else:
                valid_interval.append([i])

        presum = [0]
        index_to_position = {}
        for i in range(len(valid_interval)):
            for j in valid_interval[i]:
                index_to_position[j] = i

            L = len(valid_interval[i])
            presum.append(presum[-1] + L * (L+1) // 2)
        
        res = []
        for l, r in queries:
            ll, rr = index_to_position[l], index_to_position[r]
            if ll == rr:
                L = r-l+1
                res.append(L * (L+1) // 2)
                continue

            L1 = valid_interval[ll][-1] - l + 1
            L2 = r - valid_interval[rr][0] + 1

            count = L1 * (L1+1)//2 + L2 * (L2+1)//2
            count += presum[rr] - presum[ll+1]
            res.append(count)
        return res