"""
classic Greedy Bitwise challenge.

To maximize the bitwise AND of a subset, we need to try and set the highest bits (most significant bits) to $1$ whenever possible, as a $1$ in a higher bit is always more valuable than any combination of $1$s in lower bits.

The Strategy: Greedy Bitwise Construction
We build our result (res) from bit $30$ down to $0$. For each bit, we ask: "Can we pick $m$ numbers and increment them such that all $m$ numbers have all the bits of (res | (1 << bit)) set to $1$ within our budget $k$?"

Why this works:

1. High-to-Low Greedy: If we can satisfy the condition for bit $j$, we should always take it. Even if taking bit $j$ makes it harder to take bits $j-1, j-2, \dots, 0$, the value $2^j$ is greater than $\sum_{i=0}^{j-1} 2^i$.
2. Cost Calculation: To make a number num satisfy a target bitmask res, we need to find the smallest number $X \ge \text{num}$ such that $(X \ \& \ \text{res}) == \text{res}$.
    - The cost to achieve this is $X - \text{num}$.
    - The trick: If a number already satisfies the mask, the cost is $0$. If it doesn't, we need to "round up" the number to the next value that has all the required bits set.

How to calculate the cost efficiently

For a target mask, the smallest value $X \ge \text{num}$ that satisfies $(X \ \& \ \text{mask}) == \text{mask}$ can be found by:

1. Checking which bits are in mask but missing in num.
2. However, simply adding those bits isn't enough because adding a bit might overflow into a higher bit and change the bits we've already "secured.
3. "Correct logic: To satisfy mask, any bit in num that is higher than the current bit being checked and not in the mask must be cleared or handled. But since we are only allowed to increase nums[i], we find the smallest value $X \ge \text{num}$ such that $(X \ \& \ \text{mask}) == \text{mask}$.


Why costs.sort()?
At each bit level, we want to see if it's possible to satisfy the current res for at least m numbers. 
Sorting the costs and picking the m smallest ensures we are checking the minimum possible expenditure of k to achieve that bit.
"""

class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        res = 0
        
        # Iterate from the 30th bit down to 0
        for b in range(30, -1, -1):
            target = res | (1 << b)
            
            costs = []
            for x in nums:
                # We need to find the smallest Y >= x such that (Y & target) == target
                # This is a bitwise trick:
                # 1. Start with the bits of x that are already at or above target
                # 2. Or, use a simpler greedy approach for the cost:
                
                cost = 0
                current_val = x
                # If current_val already has target bits, cost is 0.
                # If not, we must increase it.
                if (current_val & target) != target:
                    # To satisfy 'target', the simplest way is to see what x
                    # looks like if we force the target bits.
                    # Specifically: (x >> b) must be increased if the bits don't match.
                    
                    # Correct cost calculation for 'at least x' with 'target bits':
                    # We only care about bits from b upwards for the current greedy step.
                    # cost = (target - (x % (some power))) ... 
                    # Let's use the precise logic:
                    
                    # The smallest Y >= x such that (Y & target) == target:
                    # We only need to check bits from 30 down to 0.
                    # val = 0
                    # for i in range(30, -1, -1):
                    #     if (target >> i) & 1:
                    #         val |= (1 << i)
                    #     else:
                    #         # If this bit is not in target, we want to keep 
                    #         # the bit from x IF it doesn't prevent us from 
                    #         # hitting a higher target bit.
                    #         # But actually, there's a simpler way:
                    #         pass
                    
                    # Let's use the actual required math:
                    # Smallest Y >= x s.t. (Y & target) == target
                    Y = 0
                    for i in range(30, -1, -1):
                        if (target >> i) & 1:
                            Y |= (1 << i)
                        elif (Y | ((1 << i) - 1)) < x:
                            # If we don't set this bit, even if all lower bits 
                            # are 1, we are still < x. So we MUST set it.
                            Y |= (1 << i)
                    cost = Y - x
                
                costs.append(cost)
            
            costs.sort()
            # Check if the sum of the m cheapest costs is within k
            if sum(costs[:m]) <= k:
                res = target
                
        return res