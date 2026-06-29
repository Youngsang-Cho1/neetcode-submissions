# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = TreeNode()
        curr.val = val
        if root == None:
            return curr
        if val < root.val:
            if root.left == None:
                root.left = curr
            else:
                 self.insertIntoBST(root.left, val)

        elif val > root.val:
            if root.right == None:
                root.right = curr
            else:
                 self.insertIntoBST(root.right, val)
        return root



        # if < left, recursion on root.left
        # if > right, recursion on root.right
        # if null, insert


        