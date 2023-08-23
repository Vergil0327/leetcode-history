from solution import Solution

def test_solution():
    solution = Solution()
    assert(solution.longestDupSubstring("banana"), "ana")
    assert(solution.longestDupSubstring("abcd"), "")
    assert(solution.longestDupSubstring("avavavavavavava"), "avavava")