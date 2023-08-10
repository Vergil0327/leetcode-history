from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.digitsCount(1, 1, 13) == 6
    assert solve.digitsCount(3, 100, 250) == 35
    assert solve.digitsCount(3, 10, 25) == 2
