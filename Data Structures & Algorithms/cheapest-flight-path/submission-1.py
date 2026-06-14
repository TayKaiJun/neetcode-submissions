import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Dijkstra with additional constraint of length of path
        - how do we modify dijkstra's in the event a costlier path satisfy k but got discarded in favor of a lower cost
        - since priority queue will always pop lowest cumulative cost first, we just need to check if at a given node,
          are we currently exploring a path that gives fewer no. of stops?

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
        # stores min no. of flights taken to reach this node
        flightsTaken = [ float('inf') ] * n

        minHeap = [ (0, src, 0 )]
        while minHeap:
            totalCost, currentNode, stops = heapq.heappop( minHeap )
            if currentNode == dst:
                return totalCost
            # if exceed stops constraint or we already have a more efficient path with fewer stops via this node
            # we can skip evaluating this path
            if stops == k+1 or stops >= flightsTaken[currentNode]:
                continue
            
            flightsTaken[currentNode] = stops
            for dstNode, nextCost in adjList[ currentNode ]:
                pathCost = totalCost + nextCost
                # we can blindly push nodes in as if they're less efficient, they'll be pruned as above
                heapq.heappush(minHeap, (pathCost, dstNode, stops+1) )
        
        return -1
