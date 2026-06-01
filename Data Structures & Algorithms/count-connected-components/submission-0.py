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

        def bfs( node ):
            nonlocal components

            subgraph = set()
            queue = deque( [ node ] )
            while queue:
                curr = queue.popleft()
                subgraph.add(curr)
                visited.add(curr)
                for adj in adjList[curr]:
                    if adj not in subgraph:
                        queue.append(adj)
            components += 1
            
        for i in range( n ):
            if i not in visited:
                bfs( i )
            
            # not necessary but slight optimization for early termination
            if len( visited ) == n:
                return components
        
        return components
