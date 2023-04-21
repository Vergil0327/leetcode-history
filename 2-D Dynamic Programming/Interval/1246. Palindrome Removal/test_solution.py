from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.minimumMoves([1,2]) == 2
    assert solve.minimumMoves([1,3,4,1,5]) == 3
    assert solve.minimumMoves([1,3,4,4,3,4,4,1,5]) == 3
    assert solve.minimumMoves([1,3,4,4,3,1]) == 1
    assert solve.minimumMoves([1,4,3,1]) == 2
    