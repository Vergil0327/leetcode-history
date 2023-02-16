# DP + Binary Searchclass Solution:
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1) # dp[i]: the maximum number of covered prize for prizePositions[i:]
        
        res = 0
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_right(prizePositions, prizePositions[i] + k)
            dist = j - i
            res = max(res, dist+dp[j]) # dist is maximum number of prize for [i:j),  dp[j] covered [j:]
            dp[i] = max(dist, dp[i + 1])
        return res

# DP + Sliding Window
class Solution:
    def maximizeWin(self, positions: List[int], k: int) -> int:
        n = len(positions)
        dp = [0] * (n+1)

        res = l = r = 0
        while r < n:
            num = positions[r]
            r += 1

            while l < r and num-positions[l] > k:
                l += 1

            dp[r] = max(dp[r-1], r-l)
            res = max(res, r-l + dp[l])
        return res


# 3-Pass
# 遍歷一個分界點，找出分界點左邊最大區間及分界點右邊最大區間
# 遍歷全部後找最大區間即可
# 有個算是Greedy的思想是，這兩個區間當然不重合才是最好的，所以是`pre[k]+post[k+1]`
class Solution:
    def maximizeWin(self, positions: List[int], k: int) -> int:
        n = len(positions)
        if positions[-1]-positions[0] <= 2*k: return n

        pre = [0] * n
        post = [0] * n

        res = l = r = 0
        while r < n:
            num = positions[r]
            r += 1
            while l < r and num-positions[l] > k:
                l += 1
            res = max(res, r-l)
            pre[r-1] = res

        l = r = n-1
        res = 0
        while l >= 0:
            num = positions[l]
            l -= 1

            while l < r and positions[r]-num > k:
                r -= 1
            res = max(res, r-l)
            post[l+1] = res

        res = 0
        for k in range(n-1):
            res = max(res, pre[k] + post[k+1])
        return res