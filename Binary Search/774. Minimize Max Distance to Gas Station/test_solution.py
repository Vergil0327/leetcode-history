from solution import Solution

def test_solution():
    solve = Solution()
    
    assert solve.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) - 0.5 < 1e-10
    assert solve.minmaxGasDist([3,6,12,19,33,44,67,72,89,95], 2) - 14.0 < 1e-10
    assert solve.minmaxGasDist([10, 19, 25, 27, 56, 63, 70, 87, 96, 97], 3) - 9.67 < 1e-10