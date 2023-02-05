class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter1 = Counter(basket1)
        counter2 = Counter(basket2)
        arr1 = []
        arr2 = []
        for k, v in counter1.items():
            if (v + counter2[k]) % 2 != 0: return -1
            
            extra = v - (v + counter2[k])//2
            while extra > 0:
                arr1.append(k)
                extra -= 1
        
        for k, v in counter2.items():
            if (v + counter1[k]) % 2 != 0: return -1

            extra = v - (v + counter1[k])//2
            while extra > 0:
                arr2.append(k)
                extra -= 1

        arr1.sort()
        arr2.sort()

        minValue = min(min(basket1), min(basket2))
        minCost = 0
        n = len(arr1)
        for i in range(n):
            minCost += min(2*minValue, min(arr1[i], arr2[n-1-i]))
            
        return minCost