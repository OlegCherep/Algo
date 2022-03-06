class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for i in range(n)]for j in range(m)]
        for i in range(len(indices)):
            for j in range(len(indices[i])):
                if j == 0:
                    for k in range(len(matrix[j])):
                        matrix[indices[i][j]][k] += 1

                elif j == 1:
                    for k in range(len(matrix)):
                        matrix[k][indices[i][j]] += 1
        k = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 != 0:
                    k += 1

        return k