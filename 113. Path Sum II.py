# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        
        
        def dfs(node, path):
            if not node:
                return 

            current_path = path + [node.val]
            res = []

            if sum(current_path)==targetSum and not node.left and not node.right:
                res.append(current_path)
            
            if node.left:
                res.extend(dfs(node.left,current_path))
            if node.right:
                res.extend(dfs(node.right,current_path))
            return res
        
        return dfs(root,[])

        