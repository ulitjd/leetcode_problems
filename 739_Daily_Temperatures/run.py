import enum
# from solution import Solution
from my_solution import Solution

testcases = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 40, 50, 60], [1, 1, 1, 0]),
    ([30, 60, 90], [1, 1, 0]),
]

solution = Solution()

for i, tc in enumerate(testcases):
    output = solution.dailyTemperatures(tc[0])
    print(f"Testcase #{i+1} is " + ("pass" if output == tc[1] else "fail"))
