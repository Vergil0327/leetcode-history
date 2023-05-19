from solution import Solution, TreeNode

def test_solution():
    solve = Solution()

    def build(nums):
        nodes = [(TreeNode(num) if num != -1 else None) for num in nums]
        n = len(nodes)
        for i in range(n):
            if nodes[i] == None: continue
            if 2*i+1 < n:
                nodes[i].left = nodes[2*i+1]
            if 2*i+2 < n:
                nodes[i].right = nodes[2*i+2]
        return nodes[0]

    root = build([4,2,6,1,3,5,7])
    l, r = solve.splitBST(root, 2)
    
    def dfs(root):
        if not root: return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    
    res = []
    dfs(l)
    assert res == [1, 2]

    res = []
    dfs(r)
    assert res == [3, 4, 5, 6, 7]
    
    root = build([10,2,12,1,7,11,13,-1,-1,6,8])
    l, r = solve.splitBST(root, 7)

    res = []
    dfs(l)
    assert res == [1, 2, 6, 7]
    
    res = []
    dfs(r)
    assert res == [8, 10, 11, 12, 13]