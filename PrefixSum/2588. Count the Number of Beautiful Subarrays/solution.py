class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:        
        n = len(nums)
        cnt = 0
        preXOR = [0] * (n+1)
        counter = defaultdict(int)
        counter[0] = 1
        for i in range(1, n+1):
            preXOR[i] = preXOR[i-1] ^ nums[i-1]
            if preXOR[i] in counter:
                cnt += counter[preXOR[i]]
            counter[preXOR[i]] += 1
            
        return cnt