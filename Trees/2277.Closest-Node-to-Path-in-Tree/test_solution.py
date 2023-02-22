from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.closestNode(7, [[0,1],[0,2],[0,3],[1,4],[2,5],[2,6]], [[5,3,4],[5,3,6]]) == [0,2]
    assert solve.closestNode(3, [[0,1],[1,2]], [[0,1,2]])
