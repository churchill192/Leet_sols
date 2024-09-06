# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(node):
            if node is None:
                return None
            else:
                current_node = node
                result = []
                queue = []
                queue.append(current_node)
                while len(queue)>0:
                    list1 = []
                    for i in range(len(queue)):
                        current_node = queue.pop(0)
                        list1.append(current_node.val)
                        if current_node.left:
                            queue.append(current_node.left)
                        if current_node.right:
                            queue.append(current_node.right)
                    
                    result.append(list1)
                
                return reversed(result)
        
        return bfs(root)
        