# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def bfs(node):
            if node is None:
                return None
            else:
                result = []
                queue = []
                current_node = node
                queue.append(current_node)
                while len(queue)>0:
                    list1=[]
                    for i in range(len(queue)):
                        current_node = queue.pop(0)
                        list1.append(current_node.val)
                        if current_node.left:
                            queue.append(current_node.left)
                        if current_node.right:
                            queue.append(current_node.right)
                    
                    result.append(sum(list1))
                
                return result[-1]
        return bfs(root) 

        