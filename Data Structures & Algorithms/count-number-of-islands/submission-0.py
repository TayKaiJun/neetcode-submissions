class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def legal( r, c )->bool:
            if 0 <= r < n and 0 <= c < m:
                return True
            return False
        
        directions = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0],
        ]

        def dfs( r, c ):
            if grid[r][c] == '1':
                grid[r][c] = '.'

            for dx, dy in directions:
                newR = dx+r
                newC = dy+c

                if legal( newR, newC) and grid[newR][newC] == '1':
                    dfs( newR, newC)
        
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    islands += 1
                    dfs( i, j )

        return islands