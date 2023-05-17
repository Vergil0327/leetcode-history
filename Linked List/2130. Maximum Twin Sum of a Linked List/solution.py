# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(2n)
# space: O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            
            # reverse
            nxt = slow.next
            slow.next = prev
            prev, slow = slow, nxt
        
        res = 0
        while slow and prev:
            res = max(res, slow.val + prev.val)
            slow, prev = slow.next, prev.next
        return res

# time: O(3n)
# space: O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        prev = None
        curr = head
        i = 0
        while curr:
            i += 1
            if i > n//2-1: # reverse right half
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            else:
                curr = curr.next
        
        res = 0
        h1, h2 = head, prev
        while h1 and h2:
            res = max(res, h1.val+h2.val)
            h1, h2 = h1.next, h2.next
        return res

# time: O(2n)
# space: O(n)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        l, r = 0, len(arr)-1
        res = 0
        while l < r:
            res = max(res, arr[l]+arr[r])
            l, r = l+1, r-1
        return res