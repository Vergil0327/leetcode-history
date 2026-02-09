from bisect import bisect_left

class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        # Find the maximum value to know how many bits to check
        max_num = max(nums) if nums else 0
            
        max_bits = max_num.bit_length()
        res = 0

        # Iterate through each bit position (0 to 30)
        for bit_pos in range(max_bits):
            mask = 1 << bit_pos
            
            # Efficiently filter numbers that have this bit set
            # We only build the LIS for this specific subset
            sub_nums = [x for x in nums if (x & mask)]
            
            if not sub_nums: continue
            
            # Standard O(N log N) LIS using binary search
            tails = []
            for x in sub_nums:
                idx = bisect_left(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
            
            res = max(res, len(tails))
            
            # Optimization: if the current result is already the maximum 
            # possible length (total nums), we can stop early.
            if res == len(nums):
                break
                
        return res
    

class SolutionTLE:
    """
    Bit-Based DP:
    Since $nums[i] \leq 10^9$, there are about 30 bits to consider.
    We can use Dynamic Programming where dp[k] stores the length of the longest strictly increasing subsequence where all elements have the $k$-th bit set.
    """
    def longestSubsequence(self, nums: List[int]) -> int:
        # dp[k] = length of LIS where every element has the k-th bit set
        # and the 'last' element of that LIS is 'val'
        # We need the 'val' to ensure the "strictly increasing" property.
        # So: dp[bit] = (length, last_val)
        
        # Because we need it to be strictly increasing, 
        # a simple array for DP isn't enough because we need to know 
        # what the previous value was to ensure nums[i] > prev.
        
        # Correct DP state: dp[k] is the length of the LIS ending at some 
        # number where the k-th bit is the "shared" bit.
        
        # Since we want to maximize the total length, for each number, 
        # we check all bits that are set in it.
        
        # Let f[k] be the length of the LIS where the k-th bit is common.
        # To maintain the "strictly increasing" property, we can process 
        # unique numbers in sorted order, OR use the fact that if we 
        # iterate through the original array, we only care about 
        # sequences ending in a value smaller than the current one.
        
        # Optimization: Sort the unique numbers first? 
        # No, the problem asks for a SUBSEQUENCE (order matters).
        
        # dp[bit] will store a list of (value, length) for that bit
        # To keep it efficient, for each bit, we only care about the 
        # "best" length for a given ending value.
        
        # bits_dp[k] = list of (last_val, length)
        bits_dp = [[] for _ in range(31)]
        ans = 0
        
        for num in nums:
            current_bits = [b for b in range(31) if (num >> b) & 1]
            for b in current_bits:
                # For this bit, find the longest LIS ending in val < x
                best_prev_len = 0
                # Standard LIS optimization: since we process nums in order,
                # we just need to find max length in bits_dp[b] where val < x
                for val, length in bits_dp[b]:
                    if val < num:
                        best_prev_len = max(best_prev_len, length)
                
                new_len = best_prev_len + 1
                bits_dp[b].append((num, new_len))
                ans = max(ans, new_len)
        
        return ans
    

