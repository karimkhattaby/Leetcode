class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # set to store rows indeces which have a zero
        zero_rows = set()
        # set to store columns indeces which have a zero
        zero_cols = set()
        
        # looping through the matrix, and adding indeces to the list
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
              zero_rows.add(i)
              zero_cols.add(j)
        
        # for each row that has a 0, change all elements in that row to 0
        for i in zero_rows:
          for j in range(len(matrix[0])):
            matrix[i][j] = 0
        
        # for each column that has a 0, change all elements in that column to 0
        for j in zero_cols:
          for i in range(len(matrix)):
            matrix[i][j] = 0