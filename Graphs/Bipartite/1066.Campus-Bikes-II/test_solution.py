from solution import Solution, Solution2

def test_solution():
    solve = Solution()

    workers = [[0,0],[2,1]]
    bikes = [[1,2],[3,3]]
    expected = 6
    assert solve.assignBikes(workers, bikes) == expected
    workers = [[0,0],[1,1],[2,0]]
    bikes = [[1,0],[2,2],[2,1]]
    expected = 4
    assert solve.assignBikes(workers, bikes) == expected
    
    solve2 = Solution2()

    workers = [[0,0],[2,1]]
    bikes = [[1,2],[3,3]]
    expected = 6
    assert solve2.assignBikes(workers, bikes) == expected
    workers = [[0,0],[1,1],[2,0]]
    bikes = [[1,0],[2,2],[2,1]]
    expected = 4
    assert solve2.assignBikes(workers, bikes) == expected