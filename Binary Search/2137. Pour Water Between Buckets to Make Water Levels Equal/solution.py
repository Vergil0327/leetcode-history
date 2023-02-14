class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        l, r = 0, max(buckets)

        def enough(threshold):
            waterWeHave = 0
            waterWeNeed = 0
            for water in buckets:
                if water > threshold:
                    waterWeHave += (water-threshold)*(100-loss)/100
                else:
                    waterWeNeed += threshold-water
            return waterWeHave >= waterWeNeed

                    
        while abs(r-l) > int(1e-5):
            mid = l + (r-l)/2
            if enough(mid):
                l = mid
            else:
                r = mid
        return l