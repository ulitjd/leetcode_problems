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
    pass
