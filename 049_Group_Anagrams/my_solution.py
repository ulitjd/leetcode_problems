from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w = defaultdict(list)
        for s in strs:
            w["".join(sorted(s))].append(s)
        return list(w.values())

    def groupAnagrams_my_2(self, strs: List[str]) -> List[List[str]]:
        orda = ord("a")
        memo = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - orda] += 1
            memo[tuple(key)].append(s)
        return list(memo.values())

    def groupAnagrams_my(self, strs: List[str]) -> List[List[str]]:
        orda = ord("a")
        memo = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - orda] += 1
            skey = "".join([f"{i:>5}" for i in key])
            if skey not in memo:
                memo[skey] = []
            memo[skey].append(s)
        return list(memo.values())


solution = Solution()

output = solution.groupAnagrams_my(["aaaaaaaaaaaabbb", "abbbbbbbbbbbbbbbbbbbbbbb"])
print(output)

output = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(output)
