from solution import SolutionTopDown, SolutionBottomUp

def test_solution():
    solveByTopDown = SolutionTopDown()
    solveByBottomUp = SolutionBottomUp()

    assert solveByTopDown.minimumTime([3,1,4]) == 4
    assert solveByTopDown.minimumTime([1,1,4]) == 4    
    assert solveByTopDown.minimumTime([1,2,4,9]) == 6

    assert solveByBottomUp.minimumTime([3,1,4]) == 4
    assert solveByBottomUp.minimumTime([1,1,4]) == 4
    assert solveByBottomUp.minimumTime([1,2,4,9]) == 6