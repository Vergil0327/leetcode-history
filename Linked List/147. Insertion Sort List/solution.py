# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find size to assure how many operations we need to perform
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        
        dummy = ListNode(-inf)
        dummy.next = head
        for i in range(n-1):
            # find node we want to sort and insert 
            tail, curr = dummy, dummy.next
            for _ in range(i+1):
                tail = curr
                curr = curr.next

            # find insertion position
            prev, target = dummy, dummy.next
            while target.next != curr and target.val < curr.val:
                prev = target
                target = target.next

            # because of this condition `target.next != curr`, we need to check if curr.val <= target.val or not
            # `>=` rather than `>`, `>` can't cover duplicate
            # we need to insert for both greater than or equal to
            if target.val >= curr.val:
                tail.next = curr.next
                curr.next = target
                prev.next = curr

        return dummy.next

# Optimized
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-inf)
        dummy.next = head

        prev, curr = head, head.next
        while curr:
            # current node is already in right position
            if curr.val >= prev.val:
                prev, curr = curr, curr.next
                continue

            # find insertion position
            tmp = dummy
            while curr.val > tmp.next.val:
                tmp = tmp.next

            # insertion
            prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr

            # move current node to next
            curr = prev.next
        
        return dummy.next