import pytest
from treenode import TreeNode
from solution import Solution

solution = Solution()


# @pytest.mark.incremental
class TestGroup:
    @pytest.mark.parametrize(
        "input, nodes, expected",
        [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [7, 6, 2, 4], 5),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [4, 7], 2),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [1], 1),
        ],
    )
    def test_closest_value(self, input, nodes, expected):
        root = TreeNode()._array_to_tree_node(input)
        output = solution.lowestCommonAncestor(root, nodes)
        print(f"{input = }, {output = }")
        assert output == expected
