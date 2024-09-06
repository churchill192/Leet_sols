# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def bfs(root):
            current_node = root
            if current_node is None:
                return False
            else:

                bfs_r = []
                queue = []
                queue.append(current_node)
                while len(queue) > 0:
                    current_node = queue.pop(0)
                    bfs_r.append(current_node.val)
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                    else:
                        bfs_r.append(None)
                return bfs_r
        
        x = bfs(p)
        y = bfs(q)
        if x == y:
            return True
        else:
            return False
            