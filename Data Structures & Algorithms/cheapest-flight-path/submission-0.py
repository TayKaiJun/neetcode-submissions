import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Dijkstra with additional constraint of length of path
        - how do we modify dijkstra's in the event a costlier path satisfy k but got discarded in favor of a lower cost
        BFS (if we reached k+1 iterations but didnt reach destination, we know it's impossible)

                    0
             1(100)      2(300)   8
          3(100)    
                   4(100)
            5(300)      6(200)
                       7(50)   
                  5
        '''
        adjList = { i: [] for i in range(n) }
        for flight in flights:
            fromNode, toNode, cost = flight
            adjList[ fromNode ].append( [toNode, cost] )
        # stores optimal cost at each no. of stops via this node
        costs = [ [ float('inf') ] * (k+3) for _ in range(n) ]

        costs[src][0] = 0
        minHeap = [ (0, src, -1 )]
        while minHeap:
            totalCost, currentNode, stops = heapq.heappop( minHeap )
            if currentNode == dst:
                return totalCost
            # if exceed stops constraint or we already have a more efficient path at this stop count via this node
            # we can skip evaluating this path
            if stops == k or costs[currentNode][stops+1] < totalCost:
                continue
            
            for dstNode, nextCost in adjList[ currentNode ]:
                pathCost = totalCost + nextCost
                nextStop = stops+1
                if costs[dstNode][nextStop+1] > pathCost:
                    costs[dstNode][nextStop+1] = pathCost
                    heapq.heappush(minHeap, (pathCost, dstNode, nextStop) )
        
        return -1
