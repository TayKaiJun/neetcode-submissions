# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        caveat: first make sure p < q
        for BST, the LCA will always be the root of the sub-tree containing both p and q
        '''
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        
        while not p.val <= root.val <= q.val:
            if root.val > p.val and root.val > q.val:
                # left subtree
                root = root.left
            else:
                # right subtree
                root = root.right

        return root
        
