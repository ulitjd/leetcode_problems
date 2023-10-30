from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)
        return ans


"""
[73, 74, 75, 71, 69, 72, 76, 73]
[        75, 71,     72, 76, 73]
[        75,         72, 76, 73]
[        75,             76, 73]
[                        76, 73]
"""
