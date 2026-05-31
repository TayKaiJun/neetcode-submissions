# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
                  1
            2           3
              8       4   5
                    6   7
        
        post-order encoding (DFS): N N N 8 2 N N 6 N N 7 4 N N 5 3 1
        pre-order encoding: 1 2 n 8 n n 3 4 6 n n 7 n n 5 n n
        '''
        if not root:
            return ""

        encoded = []

        def dfs( curr ):
            if not curr:
                encoded.append('n')
                return
            dfs(curr.left)
            dfs(curr.right)
            encoded.append(str(curr.val))
            
        dfs( root )
        return " ".join(encoded)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''
        for post-order, decode using a stack.
        if not N, then pop past 2 nodes as the left/right children of a node.
        [N,N,N,8] -> [8] 
        [N,8,2] -> [2] 
        [2,N,N,6] -> [2,6]
        [2,6,N,N,7] -> [2,6,7]
        [2,6,7,4] -> [2,4]
        [2,4,N,N,5] -> [2,4,5]
        [2,4,5,3] -> [2,3]
        [2,3,1]->[1]

        for pre-order decode using a queue
        '''
        if not data:
            return None
        stack = []
        nodes = data.split(" ")
        
        for val in nodes:
            if val == 'n':
                stack.append(None)
            else:
                right = stack.pop()
                left = stack.pop()
                node = TreeNode( int(val), left, right )
                stack.append( node )

        return stack.pop()