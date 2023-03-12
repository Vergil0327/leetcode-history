from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.maxDepthBST([2]) == 1
    assert solve.maxDepthBST([2,1,4,3]) == 3
    assert solve.maxDepthBST([2,1,3,4]) == 3
    assert solve.maxDepthBST([1,2,3,4]) == 4