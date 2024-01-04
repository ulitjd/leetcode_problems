import pytest
from solution import Solution

solution = Solution()


# @pytest.mark.incremental
class TestGroup:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ("abcdba", True),
            ("aa", True),
            ("abcdef", False),
        ],
    )
    def test_closest_value(self, input, expected):
        output = solution.makePalindrome(input)
        assert output == expected
