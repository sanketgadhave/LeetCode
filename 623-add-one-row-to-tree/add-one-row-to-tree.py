# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def _addOneRow(root, val, depth_remaining):
            if root is None:
                return
            
            if depth_remaining == 2:
                temp_left, temp_right = root.left, root.right
                root.left, root.right = TreeNode(val, left=temp_left), TreeNode(val, right=temp_right)
                return

            _addOneRow(root.left, val, depth_remaining-1)
            _addOneRow(root.right, val, depth_remaining-1)

        if depth == 1:
            return TreeNode(val, root)

        _addOneRow(root, val, depth)
        return root