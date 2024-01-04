"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1

        while a <= b:
            i = (a + b) // 2
            curr = nums[i]

            if curr == target:
                return i

            left = nums[a]
            rght = nums[b]

            if (
                left <= target <= curr <= rght
                or rght <= left <= target <= curr
                or curr <= rght <= left <= target
                or target <= curr <= rght <= left
            ):
                b = i - 1
            else:
                a = i + 1

        return -1


solution = Solution()

output = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
print(output)

output = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
print(output)

output = solution.search([1], 0)
print(output)

output = solution.search([1, 3], 1)
print(output)
