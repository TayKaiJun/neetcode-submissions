from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Make AdjList
        Store a visited set
        while visited not all:
            BFS to explore graph
        '''
        adjList = { i: [] for i in range(n) }

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set() # global tracking of visited nodes
        components = 0
            
        for i in range( n ):
            if i not in visited:
                components += 1
                # bfs
                queue = deque( [ i ] )
                visited.add( i )
                while queue:
                    curr = queue.popleft()
                    for adj in adjList[ curr ]:
                        if adj not in visited:
                            queue.append( adj )
                            visited.add( adj )
        
        return components
