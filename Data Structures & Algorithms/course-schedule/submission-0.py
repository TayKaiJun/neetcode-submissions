from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        prereq = [[1,0],[1,2],[3,2],[4,3]]
        '''
        adjList = { i: set() for i in range(numCourses) }

        # form the adjList first (mapping nodes to the nodes it goes to)
        for reqPair in prerequisites:
            course, req = reqPair
            adjList[req].add( course )
        
        inDegrees = { i: 0 for i in range(numCourses) }
        for courses in adjList.values():
            for course in courses:
                inDegrees[course] += 1
        
        bfs = deque( course for course, degrees in inDegrees.items() if degrees == 0 )
        
        if not bfs:
            # if the queue is empty, it means that there's no nodes that has 0 indegree so a cycle must exist
            return False

        visited = set()
        while bfs:
            req = bfs.popleft()
            if req in visited:
                return False
            
            visited.add( req )
            for course in adjList[req]:
                inDegrees[course] -= 1
                if inDegrees[course] == 0:
                    bfs.append( course )

        return not bfs and len(visited) == numCourses