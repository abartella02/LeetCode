"""
Find the longest palindrome substring in the string
Expand around center of each character
    Each character is the 'center'
    How long of a palindrome can we create with that character as the 'center'
    Check for all chars
    O(n^2) time, O(1) space
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(s, start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1 : end]

        if len(s) <= 1:
            return s
        if len(s) <= 2:
            return s if s[0] == s[1] else s[0]

        palindrome = s[0]
        for i in range(0, len(s)):
            odd = expand_from_center(s, i, i)
            even = expand_from_center(s, i, i + 1)

            if len(odd) > len(even):
                palindrome = max(palindrome, odd, key=len)
            else:
                palindrome = max(palindrome, even, key=len)
        return palindrome


string = "cbbd"
s = Solution()
ans = s.longestPalindrome(string)
print(ans)
