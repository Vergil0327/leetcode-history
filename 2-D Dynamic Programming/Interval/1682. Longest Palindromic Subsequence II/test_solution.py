from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.longestPalindromeSubseq("bbabab") == 4
    assert solve.longestPalindromeSubseq("dcbccacdb") == 4