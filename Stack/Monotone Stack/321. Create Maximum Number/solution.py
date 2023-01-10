# Greedy + Monotonic Stack
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], K: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = (0,) * K

        def findMaxIn(nums, size):
            removed = len(nums)-size
            stack = []
            for num in nums:
                while stack and removed > 0 and stack[-1] < num:
                    stack.pop()
                    removed -= 1
                stack.append(num)
            return stack[:size]

        # greedily choose max one
        def merge2list(seq1, seq2):
            i, j = 0, 0
            res = []
            while i < len(seq1) or j < len(seq2):
                if i == len(seq1):
                    res.append(seq2[j])
                    j += 1
                elif j == len(seq2):
                    res.append(seq1[i])
                    i += 1
                elif seq1[i] > seq2[j]:
                    res.append(seq1[i])
                    i += 1
                elif seq2[j] > seq1[i]:
                    res.append(seq2[j])
                    j += 1
                else:
                    p, q = i, j
                    while p < len(seq1) and q < len(seq2) and seq1[p] == seq2[q]:
                        p, q = p+1, q+1
                    if p == len(seq1):
                        res.append(seq2[j])
                        j += 1
                    elif q == len(seq2):
                        res.append(seq1[i])
                        i += 1
                    elif seq1[p] > seq2[q]:
                        res.append(seq1[i])
                        i += 1
                    else:
                        res.append(seq2[j])
                        j += 1

            return tuple(res)

        
        for i in range(K+1):
            if i > m: continue
            if K-i > n: continue

            seq1 = findMaxIn(nums1, i)
            seq2 = findMaxIn(nums2, K-i)
            curr = merge2list(seq1, seq2)
            res = max(res, curr)
        
        return res

# Top-Down DP - TLE
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], K: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        
        @lru_cache(None)
        def dfs(state, i, j, k):
            if k == K: return state
            if i == m and j == n: return -inf
            
            if i == m:
                return max(dfs(state, i, j+1, k), dfs(state * 10 + nums2[j], i, j+1, k+1))
            if j == n:
                return max(dfs(state, i+1, j, k), dfs(state * 10 + nums1[i], i+1, j, k+1))
            
            return max(
                dfs(state, i+1, j, k),
                dfs(state, i, j+1, k),
                dfs(state * 10 + nums1[i], i+1, j, k+1),
                dfs(state * 10 + nums2[j], i, j+1, k+1),
            )

        maxNum = dfs(0, 0, 0, 0)
        res = []
        while maxNum:
            res.append(maxNum%10)
            maxNum //= 10
        return reversed(res)