class Solution:
    def minOperations(self, k: int) -> int:
        v = ceil(sqrt(k))
        return v - 1 + k // v - (k % v == 0)