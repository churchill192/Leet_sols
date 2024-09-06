# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def sum_of_left_leaves(node):
            if node is None:
                return None
            else:
                current_node = node
                left_leaves = []
                queue = []
                queue.append(current_node)
                while len(queue)>0:
                    current_node = queue.pop(0)
                    if current_node.left:
                        
                        if current_node.left.left is None and current_node.left.right is None:
                            left_leaves.append(current_node.left.val)
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                
                return sum(left_leaves)
        
        return sum_of_left_leaves(root)
        