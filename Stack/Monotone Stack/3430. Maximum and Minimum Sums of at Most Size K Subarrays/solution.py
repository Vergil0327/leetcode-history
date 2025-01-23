class Solution:
    def minMaxSubarraySum(self, nums, k):
        n = len(nums)
        
        def f(x):
            """
            calculate the number of valid subarrays for size from 1 to x
            """
            return 0 if x < 0 else (x+1)*x//2
        
        def count_subwindows(L, R, M):
            # left[i]: the number of valid elements to the left of nums[i]
            # right[i]: the number of valid elements to the right of nums[i]
            # L+1: the window size from left[i] + nums[i].
            # {X X X X X X} nums[i]
            #    left[i]
            # R+1: the window size from nums[i] + right[i]
            # nums[i] {X X X X X X}
            #            right[i]
            return f(M) - f(M-(L+1)) - f(M-(R+1)) + f(M-(L+1)-(R+1))
        
        def sum_of_min_subarrays_at_most_k(arr, k):
            n = len(arr)
            left = [0]*n # the number of left larger elements
            right = [0]*n # the number of right larger elements
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                left[i] = i - (stack[-1] if stack else -1) - 1
                stack.append(i)

            stack = []
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                right[i] = (stack[-1] if stack else n) - i - 1
                stack.append(i)

            total = 0
            for i in range(n):
                cnt = count_subwindows(left[i], right[i], k)
                total += arr[i]*cnt
            return total
        
        def sum_of_max_subarrays_at_most_k(arr, k):
            n = len(arr)
            left = [0]*n # the number of left smaller elements
            right = [0]*n # the number of right smaller elements
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                left[i] = i - (stack[-1] if stack else -1) - 1
                stack.append(i)

            stack = []
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                right[i] = (stack[-1] if stack else n) - i - 1
                stack.append(i)
            
            total = 0
            for i in range(n):
                cnt = count_subwindows(left[i], right[i], k)
                total += arr[i]*cnt
            return total
        
        return sum_of_min_subarrays_at_most_k(nums, k) + sum_of_max_subarrays_at_most_k(nums, k)
