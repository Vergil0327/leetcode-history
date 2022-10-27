# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = head, head
        while fast != None:
            if fast.val != slow.val:
                slow.next = None
                slow.next = fast
                slow = slow.next

            fast = fast.next
        if slow:
            slow.next = None
        return dummy.next