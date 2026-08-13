# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)

        else:
            root.left = self.insertIntoBST(root.left,val)

        return root
         





"""
NOTES


Which Order = In Oder
Root->left->Right

if root doesn't exist return it
-> if root.val < val: -> recurse right side and create a new node with that value
-> else recurse left side
-> we will be adding at leaf node

"""