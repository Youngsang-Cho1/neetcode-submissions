# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res = []
        q = deque()

        q.append([root])
        while q:
            curr = q.popleft()
            res.append([node.val for node in curr])
            level = []
            for node in curr:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                q.append(level)
        return res


        

        