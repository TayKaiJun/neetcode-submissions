from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        A tree is valid if there's no cycles in the graph & all nodes are connected as one component
        Conditions for cycle: traversing an adjacency list will
            lead to visited nodes appearing twice
        
        0 -> 1
        1 -> 0,2,3,4
        2 -> 1,3
        3 -> 1
        4 -> 1

        1->2->3->1 is cycle
        '''
        if len(edges) != n - 1:
            # tree property: there must be n-1 edges
            return False
        if n == 1:
            # edge case: 1 vertex with 0 edge is correct
            return True

        adjList = defaultdict(set)
        for edge in edges:
            v1, v2 = edge
            adjList[v1].add(v2)
            adjList[v2].add(v1)
        
        visited = set()
        def dfs( prev, curr ):
            if curr in visited:
                return False
            
            visited.add( curr )
            for adj in adjList[ curr ]:
                if adj != prev:
                    if not dfs( curr, adj ):
                        return False
            return True

        if not dfs( None, 0 ):
            return False
        
        return len( visited ) == n