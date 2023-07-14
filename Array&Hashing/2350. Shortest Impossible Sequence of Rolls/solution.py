class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = 1
        collect = set()
        for roll in rolls:
            collect.add(roll)
            if len(collect) == k:
                res += 1
                collect = set()
        return res
