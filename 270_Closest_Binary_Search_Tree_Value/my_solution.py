from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

    def make_tree(self, tree):
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


test_cases = [
    {
        "input": [
            36,
            13,
            37,
            4,
            20,
            None,
            48,
            1,
            5,
            17,
            33,
            43,
            49,
            0,
            2,
            None,
            9,
            14,
            18,
            22,
            34,
            40,
            46,
            None,
            None,
            None,
            None,
            None,
            3,
            7,
            11,
            None,
            16,
            None,
            19,
            21,
            27,
            None,
            35,
            39,
            42,
            45,
            47,
            None,
            None,
            6,
            8,
            10,
            12,
            15,
            None,
            None,
            None,
            None,
            None,
            26,
            32,
            None,
            None,
            38,
            None,
            41,
            None,
            44,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            24,
            None,
            28,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            23,
            25,
            None,
            29,
            None,
            None,
            None,
            None,
            None,
            31,
            30,
        ],
        "target": 3.142857,
        "expected": 3,
    },
    {"input": [4, 2, 5, 1, 3], "target": 3.5, "expected": 3},
    {"input": [4, 2, 5, 1, 3], "target": 4.5, "expected": 4},
    {"input": [4, 2, 5, 1, 3], "target": 3.714286, "expected": 4},
]

for tc in test_cases:
    root = TreeNode().make_tree(tc["input"])
    output = Solution().closestValue(root, tc["target"])
    print(f"{output = }")
