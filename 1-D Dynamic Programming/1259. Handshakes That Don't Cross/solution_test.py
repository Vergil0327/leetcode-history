from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.numberOfWays(2) == 1
    assert solve.numberOfWays(4) == 2
    assert solve.numberOfWays(6) == 5
    assert solve.numberOfWays(8) == 14