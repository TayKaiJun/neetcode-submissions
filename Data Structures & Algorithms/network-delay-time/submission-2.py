import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Dijkstra's is the solution
        - cost to each node starting from source
        '''
        visited = set()
        costs = [ float('inf') ] * (n+1)
        costs[k] = 0 # source node

        adjList = { i: [] for i in range(1, n+1) }
        for source, target, time in times:
            adjList[source].append( (time, target) )

        pq = [ (0,k) ]
        
        while pq:
            cumCost, target = heapq.heappop(pq)
            if target in visited:
                continue
            visited.add(target)

            costs[target] = cumCost
            for time, neighbor in adjList[target]:
                newCost = time+cumCost
                costs[neighbor] = min(costs[neighbor], newCost)
                heapq.heappush(pq, (newCost, neighbor)) 

        if len(visited) != n:
            return -1
        
        return max(costs[1:])