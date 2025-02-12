class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)
        def check(target):
            # base case: already at 0-th position
            step = 1
            score = points[0]
            
            for i in range(n):
                # edge case
                if i == n-1:
                    if score >= target: return True
                    back_forth = ceil((target-score) / points[i])
                    return step + back_forth * 2 <= m

                if score >= target:
                    step += 1
                    if step > m: return False
                    score = points[i+1]
                else:
                    back_forth = ceil((target-score) / points[i])

                    # n-2 edge case:
                    if i+1 == n-1 and points[i+1] * back_forth >= target and step+back_forth*2 <= m: # no need for further step
                        return True

                    step += back_forth*2 + 1 # 1 for forwarding to next position
                    if step > m: return False
                    score = points[i+1] * (back_forth+1)
            return True


        l, r = 0, max(points)*m
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l