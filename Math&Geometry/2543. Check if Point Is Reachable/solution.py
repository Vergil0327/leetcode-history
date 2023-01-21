# If we move from (targetX, targetY) to the points (targetX, targetY - targetX) or (targetX – targetY, targetY), the GCD of the pair remains the same
# If we move from (targetX, targetY) to the points (2 * targetX, targetY) or (targetX, 2 * targetY), the GCD of the pair remains same or gets doubled.
# Therefore, from the above observations, point (1, 1) can move to point (targetX, targetY) if and only if gcd of (targetX, targetY) is a power of 2.
# Also, x = x-y and y = y-x are the steps to find GCD(x, y). this hint us Euclidean Algorithm(輾轉相除法，求GCD用)
class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        GCD = math.gcd(targetX, targetY)

        # return GCD & (GCD-1) == 0
        while GCD %2 == 0:
            GCD //= 2
        return GCD == 1