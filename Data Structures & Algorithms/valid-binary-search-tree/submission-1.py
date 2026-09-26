# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left < less than node's key
        # right >
        # path == right -> left: check if smaller than previous, but larger than min
        # path == left -> right: check if larger than previous, but smaller than max
        # path == right -> right: if larger
        #         left -> left: if smaller
        # pass path, check right and left immedately if exist
        if not root:
            return True
        def dfs(node, lower, upper):
            if not node:
                return True
            
            if not (lower < node.val < upper):
                return False
        
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        return dfs(root, float('-inf'), float('inf')) 


'''        5
    3       7
1      4 6      8'''
            
            