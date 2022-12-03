from solution import Solution, build, TreeNode


def test_lca():
    solution = Solution()
    root = build([3,5,1,6,2,0,8,None,None,7,4])
    p, q = TreeNode(5), TreeNode(1)
    
    node = solution.lowestCommonAncestor(root, p, q)
    assert node.val == 3

    root = build([3,5,1,6,2,0,8,None,None,7,4])
    p, q = TreeNode(5), TreeNode(4)
    node = solution.lowestCommonAncestor(root, p, q)
    assert node.val == 5

    root = build([3,5,1,6,2,0,8,None,None,7,4])
    p, q = TreeNode(5), TreeNode(10)
    node = solution.lowestCommonAncestor(root, p, q)
    assert node is None

def test_build():
    nums = [3,5,1,6,2,0,8,None,None,7,4]
    root = build(nums)

    arr = []
    def dfs(root):
        if not root: return root
        
        arr.append(root.val)
        dfs(root.left)
        dfs(root.right)

        return root
    dfs(root)

    assert len(arr) == len([x for x in nums if x is not None])
    assert all(x for x in zip(arr, [num for num in nums if num is not None]))