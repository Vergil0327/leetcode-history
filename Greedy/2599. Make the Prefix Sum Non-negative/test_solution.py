from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.makePrefSumNonNegative([2,3,-5,4]) == 0
    assert solve.makePrefSumNonNegative([3,-5,-2,6]) == 1
    assert solve.makePrefSumNonNegative([-5,-3,3,-4,0,3,0,-3,4,5]) == 3