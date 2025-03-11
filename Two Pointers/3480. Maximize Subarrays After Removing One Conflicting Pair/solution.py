class Solution:
    def maxSubarrays(self, N: int, conflictingPairs: List[List[int]]) -> int:
        # Creates a data structure where right[i] contains all elements that conflict with position i and are smaller than i.
        # For each conflicting pair (a, b), it adds the smaller value to the list at index of the larger value.
        right = [[] for _ in range(N + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        # res will track the base count of valid subarrays without removing any pair
        # left is a 2-element array tracking the two most restrictive left endpoints for the current position
        #   - left = [l0, l1] tracks the maximum and second maximum left endpoint from all intervals seen thus far.
        # imp array tracks the "improvement" possible by removing each conflicting pair
        res = 0
        left = [0, 0]
        imp = [0] * (N + 1)

        # For each position r from 1 to N:
        #     - Process all conflicting elements associated with position r
        #     - Update left to contain the two largest values: the most restrictive left endpoint and the second most restrictive left endpoint
        #     max() is comparing arrays lexicographically to find the largest
        for r in range(1, N + 1):
            for l in right[r]:
                left = max(left, [l, left[0]], [left[0], l])

            # For the current position r, count valid subarrays ending at r
            # The number of valid subarrays ending at r is r - left[0] (all subarrays starting from left[0]+1 to r)
            # This gives the baseline count without removing any pair
            res += r - left[0]

            # Calculate the improvement if we remove the conflicting pair that causes the most restrictive left endpoint (left[0])
            # If we remove this pair, the left endpoint becomes left[1] (second most restrictive)
            # The improvement is the difference: left[0] - left[1] additional valid subarrays
            imp[left[0]] += left[0] - left[1]
        
        # res contains the count of valid subarrays without removing any pair
        # max(imp) finds which pair, when removed, provides the maximum improvement
        # The sum gives the maximum possible valid subarrays after removing one pair
        return res + max(imp)
