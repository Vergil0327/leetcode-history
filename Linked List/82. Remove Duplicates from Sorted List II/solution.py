# Stack
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        shouldPop = False
        while curr:
            if stack and curr.val == stack[-1].val:
                shouldPop = True
                curr = curr.next
                continue
            if shouldPop:
                stack.pop()
                shouldPop = False
                
            stack.append(curr)
            curr = curr.next
            stack[-1].next = None
        else:
            if shouldPop: stack.pop()

        dummy = ListNode()
        curr = dummy
        for node in stack:
            curr.next = node
            curr = curr.next
        return dummy.next

# In-Place
# Space-Optimized
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        d = dummy
        curr = head
        while curr and curr.next:
            if curr.val != curr.next.val:
                d.next = curr
                d = d.next
                
                curr = curr.next
                d.next = None

            else:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
        else:
            d.next = curr
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next