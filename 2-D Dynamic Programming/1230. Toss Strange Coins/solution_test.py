from solution import Solution

def test_solution():
    solve = Solution()

    prob = [0.4]
    target = 1
    expected = 0.40000
    assert solve.probabilityOfHeads(prob, target) == expected
    
    prob = [0.5,0.5,0.5,0.5,0.5]
    target = 0
    expected = 0.03125
    assert solve.probabilityOfHeads(prob, target) == expected