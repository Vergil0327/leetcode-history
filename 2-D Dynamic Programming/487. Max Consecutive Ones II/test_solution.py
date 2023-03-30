from solution import Solution, SpaceOpimizedSolution

def test_solution():
    solve = Solution()
    assert solve.findMaxConsecutiveOnes([1,0,1,1,0]) == 4
    assert solve.findMaxConsecutiveOnes([1,0,1,1,1,1,1,1,1,0]) == 9
    
    solve2 = SpaceOpimizedSolution()
    assert solve2.findMaxConsecutiveOnes([1,0,1,1,0]) == 4
    assert solve2.findMaxConsecutiveOnes([1,0,1,1,1,1,1,1,1,0]) == 9