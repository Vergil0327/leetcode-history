from solution import Solution

def test_solution():
    solve = Solution()

    nums = [4,1,5,3,1]
    k = 3
    output = 12
    assert solve.largestEvenSum(nums, k) == output

    nums = [4,6,2]
    k = 3
    output = 12
    assert solve.largestEvenSum(nums, k) == output

    nums = [1,3,5]
    k = 1
    output = -1
    assert solve.largestEvenSum(nums, k) == output
    
    nums = [1,3,5,6]
    k = 1
    output = 6
    assert solve.largestEvenSum(nums, k) == output
