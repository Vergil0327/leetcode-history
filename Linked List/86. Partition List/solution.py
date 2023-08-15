# O(n) time
# O(n) space
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first, second = deque(), deque()
        curr = head
        while curr:
            if curr.val < x:
                first.append(curr)
                curr = curr.next
                first[-1].next = None # disconnect
            else:
                second.append(curr)
                curr = curr.next
                second[-1].next = None # disconnect
        
        dummy = ListNode()
        curr = dummy
        while first:
            curr.next = first.popleft()
            curr = curr.next
        while second:
            curr.next = second.popleft()
            curr = curr.next

        return dummy.next

# Space Optimized
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, greater = ListNode(), ListNode()
        first, second = less, greater
        curr = head
        while curr:
            if curr.val < x:
                first.next = curr

                curr = curr.next
                first = first.next
            else:
                second.next = curr

                curr = curr.next
                second = second.next

        second.next = None
        first.next = greater.next
        return less.next