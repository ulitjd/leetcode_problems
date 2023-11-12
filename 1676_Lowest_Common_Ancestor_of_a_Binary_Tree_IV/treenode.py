# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

    def _array_to_tree_node(self, tree):
        root = TreeNode(tree.pop(0))
        visited = [root]

        while visited and tree:
            node = visited.pop(0)

            if not tree:
                break

            val = tree.pop(0)
            if val is not None:
                node.left = TreeNode(val)
                visited.append(node.left)

            if not tree:
                break

            val = tree.pop(0)
            if val is not None:
                node.right = TreeNode(val)
                visited.append(node.right)

        return root
