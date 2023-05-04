from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.waysToDistribute(3, 2) == 3
    assert solve.waysToDistribute(4, 2) == 7
    assert solve.waysToDistribute(20, 5) == 206085257