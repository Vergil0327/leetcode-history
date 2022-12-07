from solution import Solution


def test_solution():
    solve = Solution()
    grid1 = [
        [1,1,0,1,1],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [1,1,0,1,1],
    ]
    assert 3 == solve.numDistinctIslands(grid1)
    
    grid2 = [
        [1,1,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,1],
        [1,1,0,1,1],
    ]
    assert 2 == solve.numDistinctIslands(grid2)
    
    grid3 = [
        [1,1,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,1,0,1,1],
    ]
    assert 1 == solve.numDistinctIslands(grid3)
    
    grid4 = [
        [1,0,0,1,0],
        [1,0,0,1,0],
        [0,1,0,0,1],
        [0,1,0,0,1],
    ]
    assert 1 == solve.numDistinctIslands(grid4)
    
    grid5 = [
        [1,1,0,1,1],
        [1,0,0,1,0],
        [0,1,1,0,1],
        [0,1,0,0,1],
    ]
    assert 2 == solve.numDistinctIslands(grid5)