from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.maximumAlternatingSubarraySum([3,-1,1,2]) == 5
    assert solve.maximumAlternatingSubarraySum([2,2,2,2,2]) == 2
    assert solve.maximumAlternatingSubarraySum([1]) == 1