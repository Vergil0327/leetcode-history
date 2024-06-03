class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:        
        n, m = len(nums), ceil(log2(1e9))
        
        bits = [0]*(m+1)
        res = inf
        current = -1 # -1 in binary is '111111111'

        l = 0
        for r in range(n):
            current &= nums[r]

            for idx in range(m):
                if (nums[r] >> idx) & 1:
                    bits[idx] += 1
            
            # update the result
            res = min(res, abs(k - current))
            
            # AND values will decrease to 0 when the size of the subarray increase
            # if the current subarray AND is < k, we shrink the subarray
            while l < r and current < k:
                for idx in range(m):
                    if (nums[l]>>idx) & 1:
                        bits[idx] -= 1
                    
                    # if the current subarray has all '1' in current bit, we need to set back the AND of current bit
                    # current subarray nums[l + 1: r + 1]
                    # length == r - l
                    if bits[idx] == r - l:
                        current |= (1 << idx)

                # update the result
                res = min(res, abs(k - current))
                l += 1
                
        return res