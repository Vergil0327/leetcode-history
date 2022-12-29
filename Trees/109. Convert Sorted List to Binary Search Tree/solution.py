# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        inorder = []
        curr = head
        while curr:
            inorder.append(curr.val)
            curr = curr.next

        def build(l, r):
            if l > r: return None
            if l == r: return TreeNode(inorder[l])

            mid = l + (r-l)//2
            root = TreeNode(inorder[mid])
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root

        root = build(0, len(inorder)-1)
        return root

# Space Optimized
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next

        def build(l, r):
            nonlocal head
            if l > r: return None

            mid = l + (r-l)//2
            left = build(l, mid-1)

            # inorder

            root = TreeNode(head.val)
            root.left = left

            head = head.next

            root.right = build(mid+1, r)
            return root

        root = build(0, size-1)
        return root