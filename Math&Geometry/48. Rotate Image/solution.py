class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r0, r1 = 0, len(matrix)-1
        while r0 < r1:
            matrix[r0], matrix[r1] = matrix[r1], matrix[r0]
            r0, r1 = r0+1, r1-1

        # transpose
        for r in range(0, len(matrix)):
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
