from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ["1","1","1","1","0"],
        # ["1","1","0","1","0"],
        # ["1","1","0","0","0"],
        # ["0","0","0","0","0"]
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.bfs(grid, r, c)
                    islands += 1
        return islands

    def bfs(self, grid, r, c):
        if c < 0 or r < 0: return
        rows, cols = len(grid), len(grid[0])
        if c >= cols or r >= rows or grid[r][c] != '1': return
        grid[r][c] = '#'
        if r != 0:
            self.bfs(grid, r - 1, c)
        if r != rows - 1:
            self.bfs(grid, r + 1, c)
        if c != 0:
            self.bfs(grid, r, c - 1)
        if c != cols - 1:
            self.bfs(grid, r, c + 1)


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r not in range(rows) or
                    c not in range(cols) or
                    grid[r][c] == "0" or (r, c) in visit):
                return

            visit.add((r, c))
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, cr in direction:
                dfs(r + dr, c + cr)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)

        return islands


obj = Solution1()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(obj.numIslands(grid=grid))
