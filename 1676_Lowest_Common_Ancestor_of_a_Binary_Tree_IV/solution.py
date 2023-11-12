# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

from typing import Optional
from treenode import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        def dp(root: TreeNode) -> int | None:
            if root is None:
                return None

            if root.val in nodes:
                return root.val

            left_lca = dp(root.left)
            right_lca = dp(root.right)

            return (
                root.val
                if left_lca and right_lca
                else left_lca
                if left_lca
                else right_lca
            )

        return dp(root)


if __name__ == "__main__":
    test_cases = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [7, 6, 2, 4], 5),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [4, 7], 2),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [1], 1),
    ]
    for t in test_cases:
        root = TreeNode()._array_to_tree_node(t[0])
        nodes = t[1]
        output = Solution().lowestCommonAncestor(root, nodes)
        print(f"{output = }")
