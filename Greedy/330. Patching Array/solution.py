class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 1   -> covered 1
        # 1,2 -> covered 1,2,3
        # 1,2,3 -> covered 1,2,3,4,5,6
        # since 1,2,3 can covered 1~6, if we add 4, it means we add 4,(4+1),(4+2),(4+3),(4+4),(4+5),(4+6)
        # therefore, we maintain current max sum

        covered = 1
        count = 0
        i = 0
        while covered <= n:
            if i < len(nums) and nums[i] <= covered:
                covered += nums[i]
                i += 1
            else:
                covered += covered
                count += 1
        return count