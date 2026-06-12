from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        DSU algo
        '''
        islands = n
        dsu = DSU(n)
        for i,j in edges:
            if dsu.union(i, j):
                islands -= 1
        return islands

class DSU:
    def __init__( self, vertices ):
        self.parent = [ i for i in range(vertices) ]
        self.rank = [1] * vertices
    
    def find( self, i ):
        if self.parent[i] != i:
            self.parent[i] = self.find( self.parent[i] )
        return self.parent[i]
    
    def union( self, i, j ):
        p1 = self.find(i)
        p2 = self.find(j)
        # if p1 == p2, means they are already in unioned
        if p1 != p2:
            if self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            elif self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            else:
                self.parent[p1] = p2
                self.rank[p2] += 1
            return True
        return False
