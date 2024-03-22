# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head

        def dfs(right):
            nonlocal left
            if not right: return True
            isPalindrome = dfs(right.next)
            isPalindrome = isPalindrome and right.val == left.val
            if isPalindrome:
                left = left.next
            return isPalindrome
        return dfs(head)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        # compare side-by-side
        h1, h2 = head, prev
        while h1 and h2:
            if h1.val != h2.val: return False
            h1, h2 = h1.next, h2.next
        return True
