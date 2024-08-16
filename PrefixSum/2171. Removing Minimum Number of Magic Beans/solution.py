class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        count = Counter(beans)

        arr = [[num, cnt] for num, cnt in count.items()]
        arr.sort()
        n = len(arr)
        if n == 1: return 0 # edge case

        res = sum(beans)

        presum = [0] * (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + arr[i][0] * arr[i][1]

        accumulate = 0
        for i in range(n-1, -1, -1):
            res = min(res, accumulate + presum[i])

            accumulate += (arr[i][0]-arr[i-1][0]) * arr[i][1]
            arr[i-1][1] += arr[i][1]

        return res
