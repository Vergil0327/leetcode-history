class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        # once we break the while-loop, we found common prefix,
        # and we just shift it back
        return left<<shift
