import pytest
from solution import Solution

# from my_solution import Solution

solution = Solution()

# @pytest.mark.incremental
class TestGroup:
    @pytest.mark.parametrize(
        "input, output",
        [
            ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
            ([30, 40, 50, 60], [1, 1, 1, 0]),
            ([30, 60, 90], [1, 1, 0]),
        ],
    )
    def test_daily_temperatures(self, input, output):
        print(f"{input =}")
        assert solution.dailyTemperatures(input) == output
