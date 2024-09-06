# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def bfs(node):
            if node is None:
                return 0
            else:
                current_node = node
                avg=[]
                queue = []
                queue.append(current_node)
                while len(queue)>0:
                    in_avg = []
                    for i in range(len(queue)):
                        current_node = queue.pop(0)
                        in_avg.append(current_node.val)
                        if current_node.left:
                            queue.append(current_node.left)
                        if current_node.right:
                            queue.append(current_node.right)
                    
                    avg.append(sum(in_avg)/len(in_avg))
                return avg
        
        return bfs(root)