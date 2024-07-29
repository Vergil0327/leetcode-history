from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        # find rating[i] < rating[j] < rating[k]
        left, right = SortedList(), SortedList(rating)
        res = 0
        for j in range(n):
            cur = rating[j]

            right.remove(cur)
            i = left.bisect_right(cur)
            k = len(right) - right.bisect_left(cur)
            res += i * k
            left.add(cur)
        
        # find rating[i] > rating[j] > rating[k]
        left, right = right, left
        for j in range(n):
            cur = rating[j]

            right.remove(cur)
            i = len(left) - left.bisect_left(cur)
            k = right.bisect_right(cur)
            res += i * k
            left.add(cur)
        return res
