from solution import Solution

def test_solution():
    solve = Solution()
    sentence = "i love leetcode"
    # k = 12
    # assert solve.minimumCost(sentence, k) == 36
    
    sentence = "apples and bananas taste great"
    k = 7
    assert solve.minimumCost(sentence, k) == 21
    
    sentence = "a"
    k = 5
    assert solve.minimumCost(sentence, k) == 0
