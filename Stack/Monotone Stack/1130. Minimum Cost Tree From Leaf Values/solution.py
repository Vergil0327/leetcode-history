# O(n^3logn)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)

        dp = [[inf]*n for _ in range(n)]

        # length = 1
        for i in range(n):
            dp[i][i] = 0

        for length in range(2 ,n+1):
            for i in range(n-length+1): # j = i+length-1 < n
                j = i+length-1

                lmax = -inf
                maxHeap = [(-num, i) for i, num in enumerate(arr[i:j+1])]
                heapq.heapify(maxHeap)

                for k in range(i, j):
                    lmax = max(lmax, arr[k])
                    
                    while maxHeap and maxHeap[0][1] <= k:
                        heapq.heappop(maxHeap)
                    rmax = -maxHeap[0][0]

                    dp[i][j] = min(dp[i][j], dp[i][k] + lmax * rmax + dp[k+1][j])

        return dp[0][n-1]

# O(n)

# three-pass
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
      n = len(arr)
      prevGreater, nextGreater = [inf]*n, [inf]*n

      stack = []
      for i, num in enumerate(arr):
        while stack and arr[stack[-1]] <= num:
          nextGreater[stack.pop()] = num
        stack.append(i)

      stack.clear()
      for i, num in enumerate(arr):
        while stack and arr[stack[-1]] <= arr[i]:
          stack.pop()

        if stack:
          prevGreater[i] = arr[stack[-1]]

        stack.append(i)
      
      res = 0
      for i in range(n):
        cost = arr[i] * min(prevGreater[i], nextGreater[i])
        if cost != inf:
            res += cost
      return res

# one-pass
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [inf]
        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                res += mid * min(stack[-1], num) # stack[-1]: previous greater value; num: next greater value

            stack.append(num)

        # stil exist some value without next greater element
        while len(stack) > 2:
            mid = stack.pop()
            res += mid * stack[-1] # stack[-1]: previous greater
        return res