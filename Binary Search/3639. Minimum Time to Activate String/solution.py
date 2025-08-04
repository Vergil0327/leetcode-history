
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total_subarr = n * (n+1) // 2
        def count(t):
            position = []
            for i in range(t+1):
                position.append(order[i])
            position.sort()
            m = len(position)
            
            left_invalid = 0 if not position else (position[0] * (position[0]+1) // 2)
            right_invalid = 0 if not position else ((n-1-position[-1]) * (n-1-position[-1]+1) // 2)
            mid_invalid = 0
            for i in range(1, m):
                length = position[i]-position[i-1]-1
                mid_invalid += length * (length+1) // 2
            return total_subarr - mid_invalid - left_invalid - right_invalid

        l, r = 0, len(order)
        while l < r:
            mid = l + (r-l)//2
            x = count(mid)

            if x < k:
                l = mid+1
            else:
                r = mid
        return l if l < len(order) else -1
