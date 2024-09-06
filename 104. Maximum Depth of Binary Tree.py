# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        
        
        def bfs(node):
            current_node = node
            if current_node is None:
                return 0
            else:
                bfs_list=[]
                queue = []
                count = 0 
               
               
               
                queue.append(current_node)
                while len(queue)>0:
                    
                    count +=1
                    for i in range(len(queue)):
                        current_node = queue.pop(0)

                        if current_node.left:
                            queue.append(current_node.left)
                            
                            
                        if current_node.right:
                            queue.append(current_node.right)
                        
                    
                    
                        
                return count
        
        return bfs(root)