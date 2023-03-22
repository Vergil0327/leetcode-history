from solution import Solution

def test_solution():
    solve = Solution()
    team = [0,1,0,1,0]
    dist = 3
    output= 2
    assert solve.catchMaximumAmountofPeople(team, dist) == output

    team = [1]
    dist = 1
    output= 0
    assert solve.catchMaximumAmountofPeople(team, dist) == output
    
    team = [0]
    dist = 1
    output= 0
    assert solve.catchMaximumAmountofPeople(team, dist) == output