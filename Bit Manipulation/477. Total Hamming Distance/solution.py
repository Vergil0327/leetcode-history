class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            oneCnt = zeroCnt = 0
            for num in nums:
                if (num>>i)&1:
                    oneCnt += 1
                else:
                    zeroCnt += 1
            res += oneCnt * zeroCnt
        return res

# TLE Brute Force
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(counter)
        res = 0
        keys = list(counter.keys())
        for i in range(n):
            for j in range(i+1, n):
                res += bin(keys[i]^keys[j]).count("1") * counter[keys[i]] * counter[keys[j]]
        return res
