from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)

        sum_nums = [0] * (max_num + 1)
        sub_max = [0] * (max_num + 1)

        for n in nums:
            sum_nums[n] += n

        sub_max[1] = sum_nums[1]

        for i in range(2, len(sum_nums)):
            sub_max[i] = max(sub_max[i - 1], sum_nums[i] + sub_max[i - 2])

        return sub_max[-1]

    def deleteAndEarn_slow(self, nums: List[int]):
        max_num = max(nums)

        area = [0] * (max_num + 1)
        memo = [-1] * (max_num + 1)

        for n in nums:
            area[n] += n

        def dfs(num):
            if num < 0:
                # return 0 when out of range
                return 0

            if memo[num] < 0:
                # never visited node (num >= 0 and memo[num] < 0)
                # pick the neightbor instead of itself,
                # or pick itself with the next of the next neightbor
                memo[num] = max(dfs(num - 1), dfs(num - 2) + area[num])

            return memo[num]

        return dfs(max_num)


testcases = [
    {
        "input": [
            10,
            8,
            4,
            2,
            1,
            3,
            4,
            8,
            2,
            9,
            10,
            4,
            8,
            5,
            9,
            1,
            5,
            1,
            6,
            8,
            1,
            1,
            6,
            7,
            8,
            9,
            1,
            7,
            6,
            8,
            4,
            5,
            4,
            1,
            5,
            9,
            8,
            6,
            10,
            6,
            4,
            3,
            8,
            4,
            10,
            8,
            8,
            10,
            6,
            4,
            4,
            4,
            9,
            6,
            9,
            10,
            7,
            1,
            5,
            3,
            4,
            4,
            8,
            1,
            1,
            2,
            1,
            4,
            1,
            1,
            4,
            9,
            4,
            7,
            1,
            5,
            1,
            10,
            3,
            5,
            10,
            3,
            10,
            2,
            1,
            10,
            4,
            1,
            1,
            4,
            1,
            2,
            10,
            9,
            7,
            10,
            1,
            2,
            7,
            5,
        ],
        "output": 338,
    },
    {"input": [3, 4, 2], "output": 6},
    {"input": [2, 2, 3, 3, 3, 4], "output": 9},
]

if __name__ == "__main__":
    s = Solution()
    for t in testcases:
        output = s.deleteAndEarn(t["input"])
        print(f'{output = }  expected = {t["output"]}')

"""
Constraints:

1 <= nums.length <= 2 * 10 ** 4
1 <= nums[i] <= 10 ** 4

"""
