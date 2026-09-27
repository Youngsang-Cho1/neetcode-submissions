# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: # when we went all the way down and found no such node
            return None
        if root.val > p.val and root.val > q.val: # when both on the left side
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val: # when both on the right side
            return self.lowestCommonAncestor(root.right, p, q)
        else: # when they split -> current node is their lowest common ancestor.
            return root


        