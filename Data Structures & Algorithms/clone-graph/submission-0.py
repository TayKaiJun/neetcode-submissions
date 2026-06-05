"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        map each val to its pointer?
        '''
        if not node:
            return None

        cloned = {}

        queue = collections.deque( [] )
        newRoot = Node( node.val )
        cloned[node.val] = newRoot
        for n in node.neighbors:
            queue.append((n, newRoot))
        
        while queue:
            curr, last = queue.popleft()
            if curr.val not in cloned:
                newNode = Node( curr.val )
                cloned[curr.val] = newNode
            
            newNode = cloned[curr.val]
            # update the neighbor of the last node
            last.neighbors.append( newNode )
            newNode.neighbors.append( last )

            for n in curr.neighbors:
                if n.val not in cloned:
                    queue.append((n, newNode))

        return newRoot