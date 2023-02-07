from solution import Solution, BinarySearchSolution

def test_solution():
    solve = Solution()
    assert solve.maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]) == 4
    assert solve.maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]) == 2
    assert solve.maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]) == 3

    solve2 = BinarySearchSolution()
    assert solve2.maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]) == 4
    assert solve2.maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]) == 2
    assert solve2.maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]) == 3