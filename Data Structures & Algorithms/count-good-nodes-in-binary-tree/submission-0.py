# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:   
        def dfs(root, current_max):
            if not root:
                return 0
            current = 0
            if root.val >= current_max:
                current = 1
            left, right = 0, 0
            if root.left:
                left = dfs(root.left, max(current_max, root.val))
            if root.right:
                right = dfs(root.right, max(current_max, root.val))
            return current + left + right
        return dfs(root, root.val)