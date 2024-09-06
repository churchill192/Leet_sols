# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1=[]

        def inorder_traversal(node, list1):

            if node:
                inorder_traversal(node.left, list1)
                list1.append(node.val)
                inorder_traversal(node.right, list1)

        inorder_traversal(root1, list1)
        inorder_traversal(root2, list1)
        return(sorted(list1))
        
        