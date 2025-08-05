# increasing -> decreasing -> increasing
# 找出所有decreasing區間, 然後左右延伸, 試著讓整體的sum變大

# 至於為什麼這樣行得通是因為, 對於每段decreasing來說, 左右延伸出去必定碰到下個decreaasing區間便停止
# 所以同一段increasing區間, 只會至多被左右的decreasing區間遍歷兩次
# 因此只有O(2n)的時間複雜度

class Solution:
    """
    Intuition and Concept

    Problem: Find the maximum sum of a contiguous subarray that forms a "trionic" pattern: an increasing sequence, followed by a decreasing sequence, followed by another increasing sequence.
    Approach: Identify all decreasing intervals in the array, as they form the core of the trionic pattern. For each decreasing interval, extend it leftward (to form the first increasing part) and rightward (to form the second increasing part) to maximize the sum.
    Why It Works: Each decreasing interval is extended until it hits another decreasing interval or the array's boundaries. Since each array position is part of at most two such extensions (one from the left and one from the right), the total time complexity is O(2n).
    """
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Find all decreasing intervals [l, r] with their sums
        decreasing_intervals = []
        i = 0
        while i < n:
            total = nums[i]
            j = i
            # Scan for decreasing sequence
            while j + 1 < n and nums[j] > nums[j + 1]:
                j += 1
                total += nums[j]

            if i < j:  # Valid decreasing interval found
                if i > 0 and j < n - 1:  # Ensure extendable on both sides
                    decreasing_intervals.append((i, j, total))
                i = j
            else:
                i += 1

        res = -float('inf')
        for l, r, total in decreasing_intervals:
            # Check if extendable with increasing sequences on both sides
            if nums[l - 1] < nums[l] and nums[r + 1] > nums[r]:
                total += nums[l - 1] + nums[r + 1]
                l -= 1
                r += 1

                # Extend left (increasing) to maximize sum
                left_sum = total
                while l - 1 >= 0 and nums[l - 1] < nums[l]:
                    l -= 1
                    left_sum += nums[l]
                    total = max(total, left_sum)
                
                # Extend right (increasing) to maximize sum
                right_sum = total
                while r + 1 < n and nums[r + 1] > nums[r]:
                    r += 1
                    right_sum += nums[r]
                    total = max(total, right_sum)

                res = max(res, total)
        return res