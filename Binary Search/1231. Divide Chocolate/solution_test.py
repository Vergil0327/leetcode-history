from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5) == 6
    assert solve.maximizeSweetness([5,6,7,8,9,1,2,3,4], 8) == 1
    assert solve.maximizeSweetness([1,2,2,1,2,2,1,2,2], 2) == 5