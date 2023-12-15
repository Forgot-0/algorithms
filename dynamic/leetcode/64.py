from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]

        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                  grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        return grid[-1][-1]

l = [[1,3,1],[1,5,1],[4,2,1]]
l1 = [[1,2,3],[4,5,6]]
print(minPathSum(l))