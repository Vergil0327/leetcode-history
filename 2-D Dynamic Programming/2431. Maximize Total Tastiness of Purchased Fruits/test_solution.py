from solution import Solution

def test_solution():
    solve = Solution()

    price = [10,20,20]
    tastiness = [5,8,8]
    maxAmount = 20
    maxCoupons = 1
    assert solve.maxTastiness(price, tastiness, maxAmount, maxCoupons) == 13

    price = [10,15,7]
    tastiness = [5,8,20]
    maxAmount = 10
    maxCoupons = 2
    assert solve.maxTastiness(price, tastiness, maxAmount, maxCoupons) == 28