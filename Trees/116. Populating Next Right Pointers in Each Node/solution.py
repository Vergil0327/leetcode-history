# time: O(n)
# space: O(n)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        queue = deque([root])
        
        while queue:
            sz = len(queue)
            for i in range (sz-1):
                queue[i].next = queue[i+1]

            for _ in range(sz):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


# time: O(n)
# space: O(recursion stacks)
class SolutionFollowUpRecursion:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        if root.left:
            root.left.next = root.right
        
        if root.right:
            root.right.next = root.next.left if root.next else None

        self.connect(root.left)
        self.connect(root.right)
        
        return root

# time: O(n)
# space: O(1)
class SolutionFollowUp:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        curr = root
        while curr:
            left = curr.left
            # sub-problem - connect horizontal level
            if curr.left:
                while curr:
                    curr.left.next = curr.right
                    curr.right.next = curr.next.left if curr.next else None
                    curr = curr.next
            
            # down to next level
            curr = left
                
        return root

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""