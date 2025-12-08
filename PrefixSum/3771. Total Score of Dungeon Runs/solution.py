class Solution:    
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        # for j-th position in arr[i:j+1]:
        # hp - (pre[i] - pre[j+1]) >= requirement[j]
        # valid: hp - requirement[j] + pre[j+1] >= pre[i]
        # note. pre[j+1] = suffix_sum
        sl = SortedList()
        res = cur = 0
        for d, r in reversed(list(zip(damage, requirement))):
            sl.add(hp + cur - r)
            cur += d

            invalid = sl.bisect_left(cur)
            res += len(sl) - invalid
        return res