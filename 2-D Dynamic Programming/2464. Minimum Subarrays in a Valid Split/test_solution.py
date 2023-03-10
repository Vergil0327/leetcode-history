from solution import Solution

def test_solution():
    solve = Solution()
    
    assert solve.validSubarraySplit([2,6,3,4,3]) == 2
    assert solve.validSubarraySplit([3,5]) == 2
    assert solve.validSubarraySplit([1,2,1]) == -1