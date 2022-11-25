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

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = int(1e9+7)

        nextSmaller = [n] * n
        stack = []
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                nextSmaller[stack.pop()] = i
            stack.append(i)

        prevSmaller = [-1] * n
        stack.clear()
        for i in range(n-1, -1, -1):
            # ! important to consider duplicate num
            # ex. [3,1,2,2,2,2,4], use >= to find correct prev smaller including equal number
            while stack and arr[stack[-1]] >= arr[i]:
                prevSmaller[stack.pop()] = i
            stack.append(i)

        total = 0
        for i, num in enumerate(arr):
            # num as minimum
            # # of nums <= num in left * # of nums < num in right
            total += num * ((i-prevSmaller[i]) * (nextSmaller[i]-i)) % MOD
        return total % MOD