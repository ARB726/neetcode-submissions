# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def helperFunction(node,remainingSum):

            if not node:
                return False

            if not node.left and not node.right:
                return remainingSum == node.val

            remainingSum -=node.val

            return helperFunction(node.left,remainingSum) or helperFunction(node.right,remainingSum)

        return helperFunction(root,targetSum)     








"""
This is PostOrder as we need to pass remaining Tree to the root
left -> right -> root
"""