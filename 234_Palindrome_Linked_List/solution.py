# 234_Palindrome_Linked_ListNode
# https://leetcode.com/problems/palindrome-linked-ListNode/description/

# Definition for singly-linked ListNode.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def _list_node_to_array(self):
        lst = []
        node = self
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    @staticmethod
    def _array_to_list_node(arr):
        prev = None
        for i in arr:
            node = ListNode(i, prev)
            prev = node
        return prev


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head = head._list_node_to_array()

        print(f"{head = }")

        for i in range(len(head) // 2):
            if head[i] != head[-1 + -1 * i]:
                return False
        return True


if __name__ == "__main__":
    is_palindrome = Solution().isPalindrome
    print()
    print(is_palindrome(ListNode._array_to_list_node([1, 2, 2, 1])), end="\n\n")
    print(is_palindrome(ListNode._array_to_list_node([1, 2])), end="\n\n")
