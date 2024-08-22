class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        counts = [Counter(), Counter()]
        for i in range(n):
            counts[i%2][nums[i]] += 1

        arr1 = [[-cnt, num] for num, cnt in counts[0].items()]
        arr2 = [[-cnt, num] for num, cnt in counts[1].items()]
        heapq.heapify(arr1)
        heapq.heapify(arr2)

        cnt1, num1 = heapq.heappop(arr1)
        cnt2, num2 = heapq.heappop(arr2)
        if num1 != num2:
            return n+cnt1+cnt2
        else:
            cnt1_2nd = arr1[0][0] if arr1 else 0
            cnt2_2nd = arr2[0][0] if arr2 else 0
            return n + min(cnt2+cnt1_2nd, cnt1+cnt2_2nd)
