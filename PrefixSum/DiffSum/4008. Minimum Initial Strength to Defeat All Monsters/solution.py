class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        
        # 1. Compute total bonus B[i] for each monster using Difference Array
        diff = [0] * (n + 1)
        for l, r, v in boosts:
            diff[l] += v
            diff[r + 1] -= v
            
        bonus = [0] * n
        curr_bonus = 0
        for i in range(n):
            curr_bonus += diff[i]
            bonus[i] = curr_bonus
            
        # 2. Iterate through monsters and find the maximum required initial strength S_0
        ans = 0
        prefix_sum = 0  # Represents P_i
        
        for i in range(n):            
            # If the monster's strength exceeds the bonus, calculate required S_0
            if monsters[i] > bonus[i]:
                ans = max(ans, prefix_sum + monsters[i] - bonus[i])
                
            prefix_sum += monsters[i]
            
        return ans