class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # STEP 1: Reverse outer array
        matrix.reverse()
        
        # STEP 2: Swap inner values for each row with the column values
        for i in range (len(matrix)):
          for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]