# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dup = defaultdict(int)
        res = []
        
        def serialize(root):
            if not root: return ""
            
            left = serialize(root.left)
            right = serialize(root.right)
            
            subtree = f"{root.val},{left},{right}"
            
            if subtree not in dup:
                dup[subtree] += 1
            elif dup[subtree] == 1: # only append to result once
                res.append(root)
                dup[subtree] += 1
            return subtree  
        
        serialize(root)
        return res

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree2id = defaultdict(int)
        dup = defaultdict(int) # duplicate count
        res = []
        
        def serialize(root):
            if not root: return -1
            
            left = serialize(root.left)
            right = serialize(root.right)
            
            # since it can be very long string, we can optimize by mapping str to int and return int instead
            # and we no longer return long string at every recursion stack
            subtree = f"{root.val},{left},{right}"

            if subtree not in tree2id:
                tree2id[subtree] = len(tree2id) # uniq integer ID
                dup[subtree] += 1
            else:
                if dup[subtree] == 1: # only append to result once
                    res.append(root)
                dup[subtree] += 1
            return tree2id[subtree]
        
        serialize(root)
        return res