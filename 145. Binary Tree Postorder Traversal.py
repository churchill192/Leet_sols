# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1 = []

        def postOrder(root, list1):
            if root:
                
                if root.left:
                    postOrder(root.left,list1)
                if root.right:
                    postOrder(root.right,list1)
                list1.append(root.val)
        
        postOrder(root,list1)
        return list1
        