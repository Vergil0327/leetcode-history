from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.houseOfCards(16) == 2
    assert solve.houseOfCards(2) == 1
    assert solve.houseOfCards(4) == 0