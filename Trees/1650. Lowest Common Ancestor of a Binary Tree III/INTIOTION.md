
since we can traversal back to root by using `node.parent` field,
we can find `path from p to root` & `path from q to root`

and we start from `root` until path split, the final split node is LCA

**Other Approach**

we can think this problem as [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

- headA = p
- headB = q
- and a.next = a.parent, b.next = b.parent

```python
class Leetcode160:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```