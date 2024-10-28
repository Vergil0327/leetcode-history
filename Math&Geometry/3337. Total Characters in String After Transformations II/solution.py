class Solution:
    def mat_pow(self, matrix, n, mod):
        size = len(matrix)
        res = [[int(i == j) for j in range(size)] for i in range(size)]

        while n > 0:
            if n & 1:
                res = self.mat_mul(res, matrix, mod)
            matrix = self.mat_mul(matrix, matrix, mod)
            
            n //= 2
        return res

    def mat_mul(self, mat1, mat2, mod):
        """
        mat1      mat2
        X X X     O O O
        X X X  *  O O O = 
        X X X     O O O

        1-indexed來看的話:
        res[1][1] = sum(row1 of mat1 * col1 of mat2)
        """
        res = [[0]*len(mat2[0]) for _ in range(len(mat1))]

        for r in range(len(mat1)):
            for c in range(len(mat2[0])):
                for k in range(len(mat2)):
                    res[r][c] += mat1[r][k] * mat2[k][c]
                res[r][c] %= mod
        return res


    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7

        adjacency_list = [[0] * 26 for _ in range(26)]
        for i, num in enumerate(nums):
            for j in range(i+1, i+num+1):
                adjacency_list[i][j%26] = 1

        mat = self.mat_pow(adjacency_list, t, mod)

        count = [0] * 26
        for ch in s:
            count[ord(ch)-ord("a")] += 1
        res = self.mat_mul([count], mat, mod)

        return sum(res[0]) % mod