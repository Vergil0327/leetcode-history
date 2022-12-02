from solution import SolutionPrim, SolutionKruskal

def test_solution_prim():
    solve = SolutionPrim()
    assert 3 == solve.minCostToSupplyWater(3, [1, 2, 3], [[1,2,1],[2,3,1]])
    assert 5 == solve.minCostToSupplyWater(3, [1, 2, 13], [[1,2,1],[2,3,3]])
    assert 6 == solve.minCostToSupplyWater(3, [10, 2, 13], [[1,2,1],[2,3,3]])
    assert 35 == solve.minCostToSupplyWater(3, [10, 12, 13], [[1,2,51],[2,3,53]])

def test_solution_kruskal():
    solve = SolutionKruskal()
    assert 3 == solve.minCostToSupplyWater(3, [1, 2, 3], [[1,2,1],[2,3,1]])
    assert 5 == solve.minCostToSupplyWater(3, [1, 2, 13], [[1,2,1],[2,3,3]])
    assert 6 == solve.minCostToSupplyWater(3, [10, 2, 13], [[1,2,1],[2,3,3]])
    assert 35 == solve.minCostToSupplyWater(3, [10, 12, 13], [[1,2,51],[2,3,53]])
