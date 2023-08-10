from solution import Solution

solve = Solution()

def test_solution():
    assert solve.ipToCIDR("255.0.0.7", 10) == ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]