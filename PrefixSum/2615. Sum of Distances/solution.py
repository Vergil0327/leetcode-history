# Brute Force, TLE
class Solution_TLE:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        group = defaultdict(list)
        for i, num in enumerate(nums):
            group[num].append(i)
            
        dist = defaultdict(lambda: [0] * n)
        for k, vals in group.items():
            m = len(vals)
            for i in range(m):
                SUM = 0
                for j in range(m):
                    SUM += abs(vals[i]-vals[j])
                dist[k][vals[i]] = SUM
        
        arr = [0] * n
        for i in range(n):
            if not group[nums[i]]: continue
            arr[i] = dist[nums[i]][i]
        return arr

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        # left to right to calculate left_part
        count = defaultdict(int)
        prefix_sum = defaultdict(int)
        for i, num in enumerate(nums):
            res[i] += count[num] * i - prefix_sum[num]
            prefix_sum[num] += i
            count[num] += 1

        # right to left to calculate right_part
        count = defaultdict(int)
        post_sum = defaultdict(int)
        for i in range(n-1, -1, -1):
            res[i] += post_sum[nums[i]] - count[nums[i]] * i
            post_sum[nums[i]] += i
            count[nums[i]] += 1
        return res
