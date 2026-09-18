# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs( node, depth ):
            if not node:
                return depth
            depth += 1
            left, right = depth, depth
            
            if node.left:
                left = dfs(node.left, depth )
            if node.right:
                right = dfs(node.right, depth )
            
            return max( left, right )
            
        maxDepth = dfs( root, 0 )
        return maxDepth
            