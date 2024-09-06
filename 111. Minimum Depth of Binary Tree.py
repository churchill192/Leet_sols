# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:

            queue = []
            depth = 1

            queue.append((root,depth))
            while queue:


                current_node, d = queue.pop(0)
                if current_node.left is None and current_node.right is None:
                    return d
                
                if current_node.left:
                    queue.append((current_node.left,d+1))
                if current_node.right:
                    queue.append((current_node.right,d+1))
                
            return depth
                
        