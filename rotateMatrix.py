from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(1, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()
        
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

solution = Solution()
solution.rotate(matrix)
print(matrix)

