from solution import Solution

def test_solution():
    solve = Solution()
    assert solve.mostSimilar(5, [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], ["ATL","PEK","LAX","DXB","HND"], ["ATL","DXB","HND","LAX"]) == [0,3,0,2]
    assert solve.mostSimilar(6, [[0,1],[1,2],[2,3],[3,4],[4,5]], ["ATL","PEK","LAX","ATL","DXB","HND"], ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]) == [3,4,5,4,3,2,1]
    assert solve.mostSimilar(4, [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], ["ATL","PEK","LAX","DXB"], ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]) == [1,0,1,0,1,0,1,0]