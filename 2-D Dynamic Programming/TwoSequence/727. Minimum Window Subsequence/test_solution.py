from solution import Solution

def test_solution():
    solve = Solution()
    S = "abcdebdde"
    T = "bde"
    assert solve.minWindow(S, T) == "bcde"
    
    S = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
    T = "u"
    assert solve.minWindow(S, T) == ""
    
    S = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
    T = "mek"
    assert solve.minWindow(S, T) == "meqk"
    
    S = "jmeqqkmeqksfrsdcmsiwvaovztameqqenprpvnbstl"
    T = "mek"
    assert solve.minWindow(S, T) == "meqk"
