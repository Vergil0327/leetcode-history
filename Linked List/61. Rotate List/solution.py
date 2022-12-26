# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = deque()
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
            arr[-1].next = None # disconnect

        # edge case: null check
        if not arr: return None

        for _ in range(k%len(arr)):
            arr.appendleft(arr.pop())
        
        dummy = ListNode()
        curr = dummy
        while arr:
            curr.next = arr.popleft()
            curr = curr.next

        return dummy.next

# Space Optimized
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        # calculate total length
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next

        # curr is tail now, link tail to head
        curr.next = head
        
        # find new tail
        curr = head
        for _ in range(length-k%length-1):
            curr = curr.next
        
        tail = curr
        newHead = curr.next
        tail.next = None
        
        return newHead