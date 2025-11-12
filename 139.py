from typing import *

"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        ### use marker array to keep track of valid start points for consecutive words

        i.e.
        >>> 'c  a  t  s  a  n  d'   with dict = ['cat', 'and', 'sand']
        >>> [t, f, f, t, t, f, t]

        because both 'cat' and 'cats' are valid words, words stemming from either of these
        points are valid i.e. 'sand' is valid but 'and' is not, because if we split
        'catsand' into 'cat' and 'and', there will be a stray 's' between the words,
        and thus it cannot be segmented into a **space separated** sequence.

        also, last entry in marker array must be true if the sequence is valid, since
        we cannot have any trailing characters that are not in the dict
        i.e.
        >>> 'c  a  t  d  o  g  y'   with dict = ['cat', 'dog']
        >>> [t, f, f, t, f, t, f]
        can be split into 'cat' and 'dog' but the trailing 'y' means this is not valid
        """
        # set marker to array of false's, + 1 extra since last
        # letter needs to be a valid starting point
        marker = [False] * (len(s) + 1)
        marker[0] = True  # idx zero is a valid starting point

        i = 1  # start from idx 1
        while i <= len(s):
            j = 0
            while j < i:  # iterate from 0 ... i
                if marker[j] and s[j:i] in wordDict:
                    # if j is a valid starting point and s[j:i] is a valid word
                    marker[i] = (
                        True  # that means the point where our word ends is a valid starting point
                    )
                    break
                j += 1
            i += 1

        return marker[-1]  # remember the last letter needs to be a valid starting point


_s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = Solution()
res = s.wordBreak(_s, wordDict)
print(res)
