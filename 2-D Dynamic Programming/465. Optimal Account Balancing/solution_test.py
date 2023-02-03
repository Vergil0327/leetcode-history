from solution import BacktrackingSolution, DpSolution

def test_backtracking_solution():
    solve = BacktrackingSolution()
    
    assert solve.minTransfer([[0,1,10], [2,0,5]]) == 2
    assert solve.minTransfer([[0,1,10], [1,0,1], [1,2,5], [2,0,5]]) == 1

def test_dp_solution():
    solve = DpSolution()
    assert solve.minTransfer([[0,1,10], [2,0,5]]) == 2
    assert solve.minTransfer([[0,1,10], [1,0,1], [1,2,5], [2,0,5]]) == 1