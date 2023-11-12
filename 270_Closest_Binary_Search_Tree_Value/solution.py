from typing import Optional
from treenode import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        num = root.val
        min_dist = abs(target - num)

        while root:
            dist = abs(target - root.val)

            if dist == min_dist and root.val < num:
                num = root.val
            elif dist < min_dist:
                min_dist = dist
                num = root.val

            root = root.left if target < root.val else root.right

        return num


if __name__ == "__main__":
    pass
