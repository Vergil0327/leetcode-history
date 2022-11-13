"""
Analysis:

basically, what we are doing is sorting level by level.
after BFS is done, we sort all nodes once. -> O(nlogn)

the normal BFS part is O(E+V) = O(2n+n) = O(n), each node has 2 edges.

I think overall the time complexity is probably O(n + nlogn) = O(nlogn)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        
        cnt = 0

        while queue:
            sz = len(queue)
            
            for _ in range(sz):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # count minimum swap: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
            cnt += self.countSwaps([x.val for x in queue])
        return cnt

    # algorithm:
    # [7,6,8,5]
    # -> [5,6,8,7], i=0, 7 <-> 5
    # -> [5,6,8,7], i=1, 6 already fit
    # -> [5,6,7,8], i=2, 7 <-> 8
    # -> [5,6,7,8], i=3, 8 already fit
    # [5,6,7,8]
    # O(nlogn)
    def countSwaps(self, nums):
        target = sorted(nums)
        num2Idx = {num: i for i, num in enumerate(nums)}
        
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == target[i]: continue
            
            j = num2Idx[target[i]]
            nums[i], nums[j] = nums[j], nums[i]
            num2Idx[nums[i]] = i
            num2Idx[nums[j]] = j
            cnt += 1
        return cnt