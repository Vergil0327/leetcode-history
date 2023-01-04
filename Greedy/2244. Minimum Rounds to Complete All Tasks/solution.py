# Greedy
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        res = 0
        for cnt in counter.values():
            if cnt == 1: return -1
            res += ceil(cnt/3)
        return res