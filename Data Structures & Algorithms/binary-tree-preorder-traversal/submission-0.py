# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.Result = []


        def helperFunction(node):

            if not node: return

            self.Result.append(node.val)
            helperFunction(node.left)
            helperFunction(node.right)


        helperFunction(root)
        return self.Result