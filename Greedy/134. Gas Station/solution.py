
# start points
# i ...... k ....... j
# let's start from i to j with tank = 0
# if we ran out of gas at the moment we reached j, it means we need to have tank > 0 along the road (i to j-1),
# i.e. we gat tank > 0 in [i,j-1] interval.
# thus, any k between [i,j] can't reach j
# because if we start at k with tank = 0, we got even less gas.
# so, try starting with j+1
# 
# but we need to make sure total gas is greater than total cost
# only if this condition is true, we can say that the answer exists
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [a-b for a, b in zip(gas, cost)]
        if sum(diff) < 0: return -1 # total gas is not enough

        tank = 0
        start = 0
        for i in range(n):
            tank += diff[i]
            if tank < 0: # try start at i+1
                tank = 0
                start = i+1
        return start