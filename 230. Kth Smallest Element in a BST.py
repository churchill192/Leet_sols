# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        def bst(root):
            if not root:
                return 0
            else:
                current_node = root
                bfs_list=[]
                queue = []
                queue.append(current_node)
                while len(queue)>0:
                    current_node = queue.pop(0)
                    bfs_list.append(current_node.val)
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                
                list2 = sorted(bfs_list)
                return list2[k-1]
        
        return bst(root)


        