# Sorting + Greedy: O(nlogn)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if coins >= cost:
                res += 1
                coins -= cost
        return res

# Bucket Sort
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bucket = [0] * (100005)
        for cost in costs:
            bucket[cost] += 1

        res = 0
        for cost, cnt in enumerate(bucket):
            if coins < 0: break

            if cnt > 0:
                maxTaken = min(cnt, coins//cost)
                coins -= cost * maxTaken
                res += maxTaken
        return res
