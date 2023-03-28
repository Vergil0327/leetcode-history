from solution import Solution

def test_solution():
    solve = Solution()

    # Input: present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10
    # Output: 6
    present = [5,4,6,2,3]
    future = [8,5,4,3,5]
    budget = 10
    assert solve.maximumProfit(present, future, budget) == 6
    # Input: present = [2,2,5], future = [3,4,10], budget = 6
    # Output: 5
    present = [2,2,5]
    future = [3,4,10]
    budget = 6
    assert solve.maximumProfit(present, future, budget) == 5
    # Input: present = [3,3,12], future = [0,3,15], budget = 10
    # Output: 0
    present = [3,3,12]
    future = [0,3,15]
    budget = 10
    assert solve.maximumProfit(present, future, budget) == 0