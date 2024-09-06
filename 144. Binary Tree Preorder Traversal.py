# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        list1 = []

        def preOrder(root, list1):
            if root:
                list1.append(root.val)
                if root.left:
                    preOrder(root.left,list1)
                if root.right:
                    preOrder(root.right,list1)
        
        preOrder(root,list1)
        return list1
        