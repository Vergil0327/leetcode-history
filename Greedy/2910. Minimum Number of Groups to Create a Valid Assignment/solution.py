class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        freq = sorted(Counter(nums).values())

        res = len(nums)
        for x in range(freq[0]+1, 0, -1):
            groups = 0
            valid = True
            
            # assign to x, x-1
            for f in freq:
                a, b = f//x, f%x
                if b == 0:
                    groups += a
                elif (x-1)-b <= a:
                    groups += a+1
                else:
                    valid = False
                    break

            if valid:
                return groups
        return res
