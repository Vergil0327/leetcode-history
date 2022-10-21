class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 7+10**9
        inf = float("inf")
        
        res = 0
        arrWtBoundary = [-inf] + arr + [-inf]
        stack = []
        for i in range(len(arrWtBoundary)):
            while stack and arrWtBoundary[stack[-1]] > arrWtBoundary[i]:
                index = stack.pop()
                l, r = stack[-1], i
                res += (index-l)*(r-index)*arrWtBoundary[index]
            stack.append(i)
            
        return res%mod