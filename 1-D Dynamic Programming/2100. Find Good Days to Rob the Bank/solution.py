class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        dp = [0] * n # maximum consecutive non-increasing for prefix security[:i]
        cnt = 0
        for i in range(1, n):
            if security[i-1] >= security[i]:
                cnt += 1
            else:
                cnt = 0

            dp[i] = cnt

        res = []
        cnt = 0 # 相當於 numNonDec = [0] * n # maximum consecutive non-decreasing for suffix security[i:]
        for i in range(n-1, -1, -1):
            if i < n-1 and security[i] <= security[i+1]:
                cnt += 1
            else:
                cnt = 0
            if dp[i] >= time and cnt >= time:
                res.append(i)
        return res
