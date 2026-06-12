class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len( points )
        edges = []

        # get all edges with weights being L1-distances
        for i in range(n):
            for j in range(i+1, n):
                l1Dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append( (i, j, l1Dist) )
        
        # Kruskal's implemented using DSU
        edges.sort(key=lambda x: x[2])
        # Traverse edges in sorted order
        dsu = DSU(n)
        cost = 0
        count = 0
        for x, y, w in edges:
            
            # Make sure that there is no cycle
            if dsu.find(x) != dsu.find(y):
                dsu.union(x, y)
                cost += w
                count += 1
                if count == n - 1:
                    break
        return cost

# Disjoint set data structure
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1