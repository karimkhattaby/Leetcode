class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix))]
        return heapq.nsmallest(k, arr)[-1]