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

        # Map: Original Node -> Cloned Node
        cloned = {node: Node(node.val)}
        
        # Queue just tracks the original nodes to visit
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            # Replicate the edges for curr's clone
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    # 1. Clone the neighbor node if we haven't seen it
                    cloned[neighbor] = Node(neighbor.val)
                    # 2. Add original neighbor to queue to explore its connections later
                    queue.append(neighbor)
                
                # 3. Connect the cloned current node to the cloned neighbor
                cloned[curr].neighbors.append(cloned[neighbor])
                
        return cloned[node]