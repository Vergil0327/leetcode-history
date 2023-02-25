class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1, 1] for _ in range(n+1)]

        arr.append(arr[-1])

        for i in range(n-1, -1, -1):
            if i%2 == 0:
                if arr[i] < arr[i+1]:
                    dp[i][0] = dp[i+1][0] + 1
                elif arr[i] > arr[i+1]:
                    dp[i][1] = dp[i+1][1] + 1
            else:
                if arr[i] > arr[i+1]:
                    dp[i][0] = dp[i+1][0] + 1
                elif arr[i] < arr[i+1]:
                    dp[i][1] = dp[i+1][1] + 1

        res = 0
        for turbulents in dp:
            res = max(res, max(turbulents))
        return res