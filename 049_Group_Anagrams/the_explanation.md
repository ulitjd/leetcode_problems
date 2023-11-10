As for last week: the problem "Group Anagrams"
- You did not convert a list to a string, 
  but actually you did convert a list to a tuple
- If a list is converted to a string using
  the method you mentioned, it will result this way:
  Example:
  Input: ['aaaaaaaaaaaabbb', 'abbbbbbbbbbbbbbbbbbbbbbb']
  Output: [['aaaaaaaaaaaabbb', 'abbbbbbbbbbbbbbbbbbbbbbb']]
  Correct Output: [['aaaaaaaaaaaabbb'], ['abbbbbbbbbbbbbbbbbbbbbbb']]

Side Note:
- I believe we can debug on Leetcode, but we have to upgrade to premium to use it.
