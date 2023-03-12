from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.buildTree("2-3") == "2-3"
    assert solve.buildTree("2*3") == "2*3"
    assert solve.buildTree("3/(5*2)") == "3/5*2"
    assert solve.buildTree("2-3/(5*2)+1") == "2-3/5*2+1"
    