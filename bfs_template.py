def bfs(node):
    if node is None:
        return None
    else:
        current_node = node
        result = []
        queue = []
        queue.append(current_node)

        while len(queue) > 0:

            for i in range(len(queue)):
                current_node = queue.pop(0)
                result.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return result


return bfs(root)