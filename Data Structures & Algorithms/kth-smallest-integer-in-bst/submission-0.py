# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.Result = 0
        self.k = k

        def helperFunction(node):

            if not node:
                return

            helperFunction(node.left)
            self.k -=1
            if self.k == 0:
                self.Result = node.val
            helperFunction(node.right)

        helperFunction(root)
        return self.Result

            
        

