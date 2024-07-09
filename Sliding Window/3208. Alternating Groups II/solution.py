class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        
        alternating = 0
        for i in range(k-1):
            if colors[i%n] != colors[(i+1)%n]:
                alternating += 1
        res = int(alternating == k-1)

        for i in range(1, n):
            # remove left-most
            if colors[i] != colors[i-1]:
                alternating -= 1
            # add right-most
            if colors[(i+k-1)%n] != colors[(i+k-2)%n]:
                alternating += 1
            # check sliding window validity
            if alternating == k-1:
                res += 1
        return res
