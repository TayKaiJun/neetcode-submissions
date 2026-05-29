# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        use a queue to store nodes to process.
        each queue entry should store the ptr and its level
        - queue system will ensure that if level # is different, there's nothing left of the old level
        '''
        if not root:
            return []

        queue = deque( [] )
        solution = []
        currentLevel = []
        prevLevel = 0

        queue.append( [ root, 0 ] )
        while queue:
            curr = queue.popleft()
            ptr, level = curr

            if level != prevLevel:
                prevLevel = level
                solution.append( currentLevel )
                currentLevel = []

            if not ptr:
                continue
            
            currentLevel.append( ptr.val )
            queue.append( [ ptr.left, level + 1 ] )
            queue.append( [ ptr.right, level + 1 ] )
        
        return solution
