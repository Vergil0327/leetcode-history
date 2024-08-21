class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        count = Counter()
        left_to_right = [0] * n
        right_to_left = [0] * n

        # For each r, find the minimum valid l position
        l = 0
        for r in range(n):
            count[s[r]] += 1
            while count['0'] > k and count['1'] > k:
                count[s[l]] -= 1
                l += 1
            right_to_left[r] = l

        # For each l, find the maximum r
        r = n - 1
        count = Counter()
        for l in range(n-1, -1, -1):
            count[s[l]] += 1
            while count['0'] > k and count['1'] > k:
                count[s[r]] -= 1
                r -= 1
            left_to_right[l] = r

        # For the right indexes that has left within the query bounds, all the substrings count
        # For the right indexes that has left outside the query bounds, only substrings within the bounds will count
        # So, seperate the cases for each query
        
        presum = list(accumulate([(r - l + 1) for r, l in enumerate(right_to_left)], initial=0))
        res = []
        for l, r in queries:
            middle = min(r, left_to_right[l])
            length = middle - l + 1
            cnt = (length + 1) * length // 2
            cnt += presum[r + 1] - presum[middle + 1] # where left is within, so all the substrings count
            res.append(cnt)
        return res
