from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        topo sort: Kahn's algo
        '''
        adjList = { i: set() for i in range(numCourses) }
        inDegrees = { i: 0 for i in range(numCourses) }

        # form the adjList and calculate inDegrees
        for reqPair in prerequisites:
            course, req = reqPair
            adjList[ req ].add( course )
            inDegrees[ course ] += 1
        
        schedule = []
        visitQueue = deque( course for course, degrees in inDegrees.items() if degrees == 0 )

        while visitQueue:
            req = visitQueue.popleft()
            schedule.append( req )
            
            for course in adjList[req]:
                inDegrees[course] -= 1
                if inDegrees[course] == 0:
                    visitQueue.append( course )
        
        if len( schedule ) != numCourses:
            return []

        # note: if the queue was empty to start, it means that there's no nodes that has 0 indegree so a cycle must exist
        # schedule will still be [] so we correctly return empty array
        return schedule