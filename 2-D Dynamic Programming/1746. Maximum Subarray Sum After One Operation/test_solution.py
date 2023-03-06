from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.maximumSum([2,-1,-4,-3]) == 17
    assert solve.maximumSum([1,-1,1,1,-1,-1,1] ) == 4