class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        presum = list(accumulate(capacity, initial=0))
        n = len(capacity)
        
        res = 0
        count = defaultdict(int)
        for r in range(n):
            l = r-2
            if l >= 0:
                count[capacity[l], presum[l+1]] += 1

            # capacity[i] == capacity[j] == presum[i] - presum[j+1] (1-indexed)
            # presum[j+1] = presum[i] - capacity[i]
            target = presum[r] - capacity[r]
            res += count[capacity[r], target]
            

        return res