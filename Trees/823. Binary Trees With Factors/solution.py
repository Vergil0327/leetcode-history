class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = int(1e9+7)
        
        arr.sort()

        val2idx = {}
        for i, v in enumerate(arr):
            val2idx[v] = i

        dp = [1] * n
        # root = left * right
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i]//arr[j] in val2idx:
                    idx = val2idx[arr[i]//arr[j]]
                    dp[i] += dp[j] * dp[idx] % MOD

        return sum(dp)%MOD

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9+7
        n = len(arr)
        dp = defaultdict(int)
        for num in arr:
            dp[num] += 1
        arr.sort()
        for i in range(n):
            root = arr[i]
            for j in range(i+1):
                left = arr[j]
                if root%left != 0: continue
                right = root//left
                if right not in dp: continue
                dp[root] += dp[left]*dp[right]%mod
        
        return sum(dp.values())%mod
