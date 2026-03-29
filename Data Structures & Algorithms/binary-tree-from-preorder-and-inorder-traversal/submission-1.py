# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #把 inorder 变成 值 -> 下标
        indices = {val : idx for idx, val in enumerate(inorder)}
        #指向当前要用的根节点
        self.pre_idx = 0
        
        #构建l, r范围内的树
        def dfs(l, r):
            #如果范围空，则终止
            if l > r:
                return None
            #记录当前节点的值
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
           #创建新节点
            root = TreeNode(root_val)
            
            #用 inorder 找到左右子树边界
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)
