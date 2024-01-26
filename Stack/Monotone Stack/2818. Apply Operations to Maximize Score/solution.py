class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9+7
        
        primeScore = []
        for num in nums:
            numPrime = 0
            for p in range(2, int(sqrt(num))+1):
                if num%p == 0:
                    numPrime += 1
                    while num%p == 0:
                        num //= p
            if num > 1:
                numPrime += 1
            primeScore.append(numPrime)
        
        # stack = [5 4 3 2 1], p=3
        prevGreater = [-1]*n
        stack = []
        for i, p in enumerate(primeScore):
            while stack and primeScore[stack[-1]] < p:
                stack.pop()
            if stack:
                prevGreater[i] = stack[-1]
            stack.append(i)
            
        # stack = [5 4 3 2 1], p=3
        nextGreater = [n]*n
        stack.clear()
        for i, p in enumerate(primeScore):
            while stack and p > primeScore[stack[-1]]:
                nextGreater[stack.pop()] = i
            stack.append(i)
        
        arr = [[num, i, primeScore[i]] for i, num in enumerate(nums)]
        arr.sort(key=lambda x:(-x[0], x[1]))
        
        res = 1
        for num, i, _ in arr:
            left = i-prevGreater[i]
            right = nextGreater[i]-i

            numSubarray = left*right

            res = (res * pow(num, min(k, numSubarray), mod)) % mod
            k -= numSubarray
            if k <= 0: break

        return res
