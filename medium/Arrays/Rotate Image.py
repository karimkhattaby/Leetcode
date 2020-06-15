class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # STEP 1: Swap inner lists except middle
        for i in range(len(matrix)//2):
          matrix[i], matrix[-(i+1)] = matrix[-(i+1)], matrix[i]
        
        # STEP 2: Swap inner values for each row
        for i in range (len(matrix)):
          for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]