from solution import Solution

def test_solution():
    solve = Solution()

    assert solve.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8) == [60,68]
    assert solve.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12) == []
