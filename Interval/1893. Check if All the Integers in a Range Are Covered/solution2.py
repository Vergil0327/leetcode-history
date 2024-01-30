class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0]*52
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1

        for i in range(1, len(diff)):
            diff[i] += diff[i-1]

        for i in range(left, right+1):
            if diff[i] == 0: return False
        return True