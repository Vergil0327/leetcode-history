# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
take this as example to dry run: `dummy -> 1 -> 2 -> 3 -> 4`

step by step to simulate without while loop first:

since we need to reverse group by group:
- let's define groupPrev & groupNext to group our target linked list
- also define `prev` & `curr` pointer for us to reverse the linked list

1st: we want reverse prev & curr, so we:

  1. point `curr.next to prev` & `prev.next to groupNext`
  2. point `groupPrev.next to curr`, since `curr` becomes our new head
  3. move our `prev` & `curr` pointer to next position we want
  4. add while loop to automate this process
  5. check our our termination case, and we'll see that we need to reverse linked list until `curr` reach the end
  6. done

    gp: groupPrev, p: prev, c: curr, gn: groupNext
    d, 1, 2, 3, 4
    gp p  c  gn
  
    d, 2, 1, 3, 4
    gp c  p gn
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        groupPrev = dummy
        prev, curr = dummy, head

        while curr and curr.next:
            steps = 1
            while steps > 0:
                prev, curr = prev.next, curr.next
                steps -= 1

            groupNxt = curr.next
            curr.next, prev.next = prev, groupNxt
            groupPrev.next = curr
            groupPrev = prev
            curr = groupNxt

        return dummy.next

# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019/7-8-lines-C%2B%2B-Python-Ruby
# Here, pre is the previous node. Since the head doesn't have a previous node, I just use self instead. Again, a is the current node and b is the next node.
# To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.
class SolutionElegant:
    def swapPairs(self, head):
        dummy = ListNode()
        pre, pre.next = dummy, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return dummy.next

# https://labuladong.github.io/algo/2/19/20/
class SolutionRecursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        first = head
        second = head.next
        rest = second.next
        
        # reverse first two node
        second.next = first
        
        # keep reversing to the end and return node back
        first.next = self.swapPairs(rest)
        return second
        