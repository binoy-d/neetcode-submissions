# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(node) -> [bool, int]:
            if node is None:
                return True, 0
            left, right = balanced(node.left), balanced(node.right)
            leftBalanced, rightBalanced = left[0], right[0]
            leftHeight, rightHeight = left[1], right[1]
            height = max(leftHeight, rightHeight) + 1

            if not leftBalanced or not rightBalanced:
                return False, height
            
            return abs(leftHeight - rightHeight) <= 1, height

        return balanced(root)[0]
