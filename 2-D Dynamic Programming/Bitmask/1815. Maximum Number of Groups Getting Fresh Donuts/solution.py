class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        count = [0]*batchSize
        for num in groups:
            count[num%batchSize] += 1

        state = 0
        for m in range(batchSize):
            state |= count[m] << (m*5)

        @cache
        def dfs(i, presum, state):
            if i == len(groups): return 0

            happy = 0
            for remainder in range(batchSize):
                count = (state >> (remainder*5))%(1<<5)
                if count == 0: continue
                
                state -= 1<<(remainder*5)
                happy = max(happy, dfs(i+1, (presum+remainder)%batchSize, state))
                state += 1<<(remainder*5)
            return happy + int(presum%batchSize == 0)
        return dfs(0, 0, state)
