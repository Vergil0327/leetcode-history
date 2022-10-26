import unittest

from solution import Solution

class TestSolution(unittest.TestCase):

    def test_solution_1(self):
        solution = Solution()
        self.assertEqual(solution.solution([[[1,2],[5,6]],[[1,3]],[[4,10]]]), [[3,4]])
    
    def test_solution_2(self):
        solution = Solution()
        self.assertEqual(solution.solution([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]), [[5,6],[7,9]])
    
    def test_solution2_1(self):
        solution = Solution()
        self.assertEqual(solution.solution2([[[1,2],[5,6]],[[1,3]],[[4,10]]]), [[3,4]])
    
    def test_solution2_2(self):
        solution = Solution()
        self.assertEqual(solution.solution2([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]), [[5,6],[7,9]])
    
    def test_solution2_optimized_1(self):
        solution = Solution()
        self.assertEqual(solution.solution2_optimized([[[1,2],[5,6]],[[1,3]],[[4,10]]]), [[3,4]])
    
    def test_solution2_optimized_2(self):
        solution = Solution()
        self.assertEqual(solution.solution2_optimized([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]), [[5,6],[7,9]])

if __name__ == '__main__':
    unittest.main()