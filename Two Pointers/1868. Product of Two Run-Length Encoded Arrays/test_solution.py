from solution import Solution

def test_solution():
    solve = Solution()

    encoded1 = [[1,3],[2,3]]
    encoded2 = [[6,3],[3,3]]
    output = [[6,6]]
    assert solve.findRLEArray(encoded1,encoded2) == output

    encoded1 = [[1,3],[2,3000000],[4,30000]]
    encoded2 = [[6,3],[3,3000000],[2,10000],[3,10000],[4,10000]]
    output = [[6,3000003],[8,10000],[12,10000],[16,10000]]
    assert solve.findRLEArray(encoded1,encoded2) == output

    encoded1 = [[1,3],[2,1],[3,2]]
    encoded2 = [[2,3],[3,3]]
    output = [[2,3],[6,1],[9,2]]
    assert solve.findRLEArray(encoded1,encoded2) == output