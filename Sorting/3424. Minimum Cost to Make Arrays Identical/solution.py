class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)

        cost1 = 0
        for i in range(n):
            cost1 += abs(arr[i]-brr[i]) # op. 2

        # op.2
        arr.sort()
        brr.sort()

        cost2 = k
        for i in range(n):
            cost2 += abs(arr[i]-brr[i])
        return min(cost1, cost2)
