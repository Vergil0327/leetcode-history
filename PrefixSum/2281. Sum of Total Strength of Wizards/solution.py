class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)

        nextSmaller = [n]*n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                nextSmaller[stack.pop()] = i
            stack.append(i)

        prevSmaller = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                prevSmaller[stack.pop()] = i
            stack.append(i)

        res = 0
        presum = accumulate(strength)
        pre_presum = list(accumulate(presum, initial = 0)) # 1-indexed
        for i in range(n):
            l = prevSmaller[i]
            r = nextSmaller[i]
            left, right = i-l, r-i
            rightsum = pre_presum[r]-pre_presum[i]
            leftsum = pre_presum[i]-pre_presum[max(l, 0)] # l可能是-1 => 對應於1-indexed的0
            res += (left * rightsum - right * leftsum) * strength[i]
            res %= 1000_000_007
        return res
