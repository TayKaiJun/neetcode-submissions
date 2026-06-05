from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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

        visited = [ [False] * m for _ in range(n) ]

        def bfs( queue ):
            currArea = 0
            while queue:
                r,c = queue.popleft()
                currArea += 1
                for dx, dy in directions:
                    newR = dx+r
                    newC = dy+c

                    if legal( newR, newC) and grid[newR][newC] == 1 and not visited[newR][newC]: 
                        visited[newR][newC] = True
                        queue.append( [newR, newC] )
            return currArea

        queue = deque( [] )
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    queue.append([i,j])
                    visited[i][j] = True
                    maxArea = max(maxArea, bfs( queue ))

        return maxArea