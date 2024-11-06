class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)

        res = presum = 0
        # count[0]: number of even prefix sum
        # count[1]: number of odd prefix sum
        count = [0, 0]
        for i in range(n):
            presum += arr[i]

            if presum%2 == 0:
                res += count[1]
            else:
                res += count[0] + 1
            res %= mod

            count[presum%2] += 1
        return res