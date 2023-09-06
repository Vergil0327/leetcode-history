# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # find length of linked list
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # find each segment's length
        size = n//k
        extra = n%k
        
        res = [None for _ in range(k)]
        cur = head
        for i in range(k):
            dummy = ListNode(-1)
            p = dummy
            for _ in range(size):
                p.next = cur
                p = p.next
                cur = cur.next
            
            if extra:
                p.next = cur
                p = p.next
                cur = cur.next
                extra -= 1
            
            p.next = None
            res[i] = dummy.next

        return res