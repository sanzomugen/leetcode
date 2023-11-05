# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        root_val = root.val
        left_node_val = root.left.val
        right_node_val = root.right.val
        return root_val == left_node_val+right_node_val
        