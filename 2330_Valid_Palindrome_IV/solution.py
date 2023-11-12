# https://leetcode.com/problems/valid-palindrome-iv/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def makePalindrome(self, s: str) -> bool:
        count = 0
        n2 = len(s)//2

        if n2 <= 1:
            return True

        for i in range(n2):
            if s[i] != s[-1-i]:
                count += 1
            if count > 2:
                return False

        return count <= 2
