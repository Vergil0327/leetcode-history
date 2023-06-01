from solution import Solution

def test_solution():
    solve = Solution()

    nums = [3,4,1,7,6]
    x = 4
    y = 2
    assert solve.minOperations(nums, x, y) == 3

    nums = [1,2,1]
    x = 2
    y = 1
    assert solve.minOperations(nums, x, y) == 1