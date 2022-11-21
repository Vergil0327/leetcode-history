# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# with index
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # All integers in nums are unique
        val2idx = {v: i for i, v in enumerate(nums)}
        
        def construct(l, r):
            if l > r: return None
            if l == r: return TreeNode(nums[l])
            
            maxVal = max(nums[l: r+1])
            i = val2idx[maxVal]

            root = TreeNode(maxVal)
            root.left = construct(l, i-1)
            root.right = construct(i+1, r)

            return root
        return construct(0, len(nums)-1)

class ConciseSolution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(l, r):
            if l > r: return None
            if l == r: return TreeNode(nums[l])

            i = nums.index(max(nums[l: r+1]))
            root = TreeNode(nums[i])
            root.left = construct(l, i-1)
            root.right = construct(i+1, r)

            return root
        return construct(0, len(nums)-1)

# with array
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        if len(nums) == 1: return TreeNode(nums[0])
        
        i = nums.index(max(nums))
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])

        return root