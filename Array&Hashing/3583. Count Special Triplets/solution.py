
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)

        res = 0
        for i, mid in enumerate(nums):
            side = mid*2

            r = bisect_right(count[side], i)
            l = bisect_left(count[side], i)

            res += l * (len(count[side]) - r)
            res %= 1_000_000_007
        return res

# bucket solution
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        mx = 2 * 10**5 # nums[i] <= 10^5
        
        left = [0] * (mx + 1)
        right = [0] * (mx + 1)
        for x in nums:
            right[x] += 1
        
        res = 0
        for v in nums:
            right[v] -= 1
            need = 2 * v
            res = (res + left[need] * right[need]) % mod
            left[v] += 1
        return res