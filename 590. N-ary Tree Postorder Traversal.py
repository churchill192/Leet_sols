"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        list1 = []

        def postOrder(root, list1):
            if root:
                
                for child in root.children:
                    postOrder(child,list1)
               
                list1.append(root.val)
        
        postOrder(root,list1)
        return list1
        