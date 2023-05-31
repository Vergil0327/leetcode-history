class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        presum = [0] * (n+1)
        sumIdx = {0: 0}
        predp = [inf] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + arr[i-1]
            if (t := presum[i]-target) in sumIdx:
                predp[i] = min(i - sumIdx[t], predp[i-1])
            else:
                predp[i] = predp[i-1]
            sumIdx[presum[i]] = i

        sufsum = [0] * (n+1)
        sumIdx = {0: n}
        sufdp = [inf] * (n+1)
        for i in range(n-1, -1, -1):
            sufsum[i] = sufsum[i+1] + arr[i]
            if (t := sufsum[i]-target) in sumIdx:
                sufdp[i] = min(sufdp[i+1], sumIdx[t]-i)
            else:
                sufdp[i] = sufdp[i+1]
            sumIdx[sufsum[i]] = i

        res = inf
        for i in range(n):
            res = min(res, predp[i]+sufdp[i])

        return res if res != inf else -1
