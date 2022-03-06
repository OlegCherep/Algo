class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        k = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    k += 1
        return k