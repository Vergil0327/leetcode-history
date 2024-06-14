class Solution:
    def maxTotalReward(self, rewards: List[int]) -> int:
        arr = list(sorted(set(rewards))) # we won't select same rewards[i] twice
        dp = [0]*(arr[-1]*2+1)
        n = len(arr)

        dp_mask = 1
        for i in range(n):
            # for x in range(arr[i]):
            #     dp[arr[i] + dp[x]] = arr[i] + dp[x]

            mask = (1<<arr[i])-1
            dp_mask |= (dp_mask&mask) << arr[i]

        return dp_mask.bit_length() - 1
