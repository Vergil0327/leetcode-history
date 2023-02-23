from solution import Solution

def test_solution():
    solve = Solution()

    assert solve.countSubranges([1,2,5], [2,6,3]) == 3
    assert solve.countSubranges([0,1], [1,0]) == 4