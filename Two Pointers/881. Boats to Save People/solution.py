class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l, r = 0, n-1
        res = 0
        while l < r:
            if people[r] == limit or people[l] + people[r] > limit:
                r -= 1
                res += 1
            else:
                l, r = l+1, r-1
                res += 1
        if l == r:
            return res+1
        else:
            return res
