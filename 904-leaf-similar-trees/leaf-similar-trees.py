# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, ans):
            if not node:
                return
            if not node.left and not node.right:
                ans.append(node.val)
            dfs(node.left, ans)
            dfs(node.right, ans)
        tree1 = []
        tree2 = []
        dfs(root1, tree1)
        dfs(root2, tree2)
        return tree1==tree2
        