# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        stack = []
        for node in nodes:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
        stack.append(None)
        
        dummy = ListNode()
        curr = dummy
        for node in stack:
            curr.next = node
            curr = curr.next
        return dummy.next

# Lee215 Recursion Solution: https://leetcode.com/problems/remove-nodes-from-linked-list/discuss/2852139/JavaC%2B%2BPython-3-Line-Recursion-Solution
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        # like post-order DFS
        head.next = self.removeNodes(head.next)
        if not head.next: return head
        
        # edge case: [1,1,1,1], if head.val == head.next.val, return head
        if head.val >= head.next.val:
            return head
        else:
            return head.next
