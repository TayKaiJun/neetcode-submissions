# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        1. notice that each node, we have 5 choices:
        - take left + itself
        - take right + itself
        - only take itself
        - take left + right + itself (terminates path)
        - don't take any
        (each option must at least include itself otherwise the path cannot connect)

        2. notice that along with observation 1, we can resolve each subtree into 
        its most optimal max value at that point. For e.g.:
                 25
            10         20
                    15      5
                -5     3
        At node -5, max = -5                    (taking itself)
        At node 3, max = 3                      (taking itself)
        At node 15, max = 18 = 15+3             (taking itself + right subtree)
        At node 5, max = 5                      (taking itself)
        At node 10, max = 10                    (taking itself)
        At node 20, max = 43 = 20+15+3+5        (taking itself + left + right)
        At node 25, max = 73 = 10+25+20+15+3    (taking itself+left+right)

        3. we do postorder recursion. set up conditions for connecting path:
        returns: max ( left+itself / right+itself / itself ) or 0
        '''
        maxSum = float('-inf')

        def postOrder( node ):
            nonlocal maxSum

            leftOpt = float('-inf')
            rightOpt = float('-inf')

            if node.left:
                leftOpt = postOrder( node.left )
            if node.right:
                rightOpt = postOrder( node.right )
            
            maxSum = max( node.val, node.val+leftOpt+rightOpt, node.val+leftOpt, node.val+rightOpt, maxSum )
            return max( node.val, node.val+leftOpt, node.val+rightOpt )

        postOrder(root)
        return maxSum