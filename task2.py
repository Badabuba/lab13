class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if not node:
        return []
    result = []
    current_nodes = [node]
    future_nodes = 1
    while future_nodes:
        future_nodes = []
        for n in current_nodes:
            result.append(n.value)
            if n.left:
                future_nodes.append(n.left)
            if n.right:
                future_nodes.append(n.right)
        current_nodes = future_nodes.copy()
        
    return result