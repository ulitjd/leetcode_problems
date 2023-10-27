from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [-1] * n
        for i in range(0, n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    break
            else:
                j = i
            output[i] = j - i
        return output
