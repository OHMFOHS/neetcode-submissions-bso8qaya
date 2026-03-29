# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root1, root2):
            if not root1 and not root2:
                return True
            if not (root1 and root2) or root1.val != root2.val:
                return False
            return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)
        def dfs(root):
            if not root:
                return False
            if is_same_tree(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        return dfs(root)