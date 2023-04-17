from solution import Solution

def test_solution():
    solve = Solution()

    assert solve.encode("aaa") == "aaa"
    assert solve.encode("aaaaa") == "5[a]"
    assert solve.encode("aaaaaaaaaa") == "10[a]"
    assert solve.encode("aabcaabcd") == "2[aabc]d"
    assert solve.encode("abbbabbbcabbbabbbc") == "2[2[abbb]c]"