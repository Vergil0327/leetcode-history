from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.sortTransformedArray([-4,-2,2,4], 1, 3, 5) == [3,9,15,33]
    assert solve.sortTransformedArray([-4,-2,2,4], -1, 3, 5) == [-23,-5,1,7]
    assert solve.sortTransformedArray([-4,-2,2,4], 0, 2, 0) == [-8,-4,4,8]
    assert solve.sortTransformedArray([-4,-2,2,4], 0, -2, 0) == [-8,-4,4,8]
    