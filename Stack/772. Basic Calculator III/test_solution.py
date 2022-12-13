from solution import Solution

def test_solution():
    solve = Solution()
    solve.calculate("")

    assert solve.calculate("1 + 1") == 2
    assert solve.calculate(" 6-4 / 2 ") == 4
    assert solve.calculate("2*(5+5*2)/3+(6/2+8)") == 21
    assert solve.calculate("(2+6* 3+5- (3*14/7+2)*5)+3") == -12