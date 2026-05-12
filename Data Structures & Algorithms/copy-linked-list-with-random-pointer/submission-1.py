"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        '''
        Attempt 1: 
        - use a map to store original nodes->index
        - use a map to store index->copied nodes
        '''
        curr = head
        copyPrev = copyCurr = copyHead = None
        indices = {}
        copyIndices = {} # for debugging
        copyIndexToPtr = {}

        index = 0
        while curr:
            copyCurr = Node( curr.val, None, None )
            if copyPrev:
                copyPrev.next = copyCurr
            if not copyHead:
                copyHead = copyCurr
            
            indices[ curr ] = index
            copyIndices[ copyCurr ] = index
            copyIndexToPtr[ index ] = copyCurr

            curr = curr.next
            copyPrev = copyCurr
            copyCurr = copyCurr.next
            index += 1

            # print('indices:', indices)
            # print('copy_indices:', copyIndices)
        
        def visualizeNodes( debugPtr, indices ):
            output = []
            while debugPtr:
                output.append( [ debugPtr.val, ( indices[ debugPtr.random ] if indices and debugPtr.random else None ) ] )
                debugPtr = debugPtr.next
            print( output )

        # visualizeNodes( head, indices )
        # visualizeNodes( copyHead, copyIndices )
         
        # reset and process the random ptr in this cycle
        copyCurr = copyHead
        curr = head
        while curr:
            if curr.random:
                index = indices[ curr.random ]
                copyCurr.random = copyIndexToPtr[ index ]
            curr = curr.next
            copyCurr = copyCurr.next
        
        # visualizeNodes( copyHead, copyIndices )

        return copyHead

