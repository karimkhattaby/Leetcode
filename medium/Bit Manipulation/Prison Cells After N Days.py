class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = (N%14)+14
        while N > 0:
            current = [0] * len(cells)
            for i in range(1,7):
                current[i] = 1 - (cells[i-1] ^ cells[i+1])
            cells = current
            N-=1
        return cells