# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.Result = 0

        def helperFunction(node , low , high):

            if not node:
                return 0

            if node.val >= low and node.val <= high:
                self.Result += node.val
                helperFunction(node.left,low,high)
                helperFunction(node.right,low,high)
            
            elif node.val >=low and not node.val <= high:
                helperFunction(node.left,low,high)
            
            else:
                helperFunction(node.right,low,high)
           

        helperFunction(root , low , high)

        return self.Result
