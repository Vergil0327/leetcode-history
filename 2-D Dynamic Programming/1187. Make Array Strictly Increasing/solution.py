# dp[i]: the minimum number of operations considering arr1[:i]
# dp[i] = {(prev, operation)}
# . . . . . . . X Y
# if Y > X:
#     dp[i][j] = dp[i-1]
# else:
#     dp[i] = dp[i-1] + 1
class Solution_TLE:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))

        n = len(arr1)
        m = len(arr2)

        dp = [set() for _ in range(n+1)]

        for i in range(n):
            if i == 0:
                dp[i].add((arr1[i], 0))
                dp[i].add((arr2[0], 1))
                continue
            
            for prev, operation in dp[i-1]:
                if arr1[i] > prev:
                    dp[i].add((arr1[i], operation))
                
                j = bisect.bisect_right(arr2, prev)
                if j < m:
                    dp[i].add((arr2[j], operation+1))

        res = inf
        for _, op in dp[n-1]:
            res = min(res, op)
        return res if res != inf else -1

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))

        n = len(arr1)
        m = len(arr2)

        dp = [set() for _ in range(n+1)]

        for i in range(n):
            if i == 0:
                dp[i].add((arr1[i], 0))
                dp[i].add((arr2[0], 1))
                continue

            curr = defaultdict(lambda: inf)
            for prev, operation in dp[i-1]:
                if arr1[i] > prev:
                    curr[arr1[i]] = min(curr[arr1[i]], operation)
                    # dp[i].add((arr1[i], operation))
                
                j = bisect.bisect_right(arr2, prev)
                if j < m:
                    curr[arr2[j]] = min(curr[arr2[j]], operation+1)
                    # dp[i].add((arr2[j], operation+1))

            for k, v in curr.items():
                dp[i].add((k, v))

        res = inf
        for _, op in dp[n-1]:
            res = min(res, op)
        return res if res != inf else -1

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1:0}
        arr2 = sorted(set(arr2))

        for num in arr1:
            nextDP = collections.defaultdict(lambda: float('inf'))
            for prev in dp:
                if num > prev:
                    nextDP[num] = min(nextDP[num],dp[prev])

                j = bisect.bisect_right(arr2,prev)
                if j < len(arr2):
                    nextDP[arr2[j]] = min(nextDP[arr2[j]],dp[prev]+1)
            dp = nextDP
        if dp:
            return min(dp.values())
        return -1