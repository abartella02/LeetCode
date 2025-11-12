"""
Length of longest substring
"""


class Solution:
    def lengthOfLongestSubstringOld(self, s: str) -> int:
        seen = []
        lens = [0]
        for i in s:
            if i not in seen:
                lens[-1] += 1
                seen.append(i)
            else:
                lens.append(1)
                seen = [i]
        return max(lens)

    def lengthOfLongestSubstring(self, s: str) -> int:
        gbl_max = 0
        maps = {}
        left = 0
        for right, el in enumerate(s):
            if el in maps.keys() and maps[el] >= left:
                left = maps[el] + 1

            gbl_max = max(gbl_max, right - left + 1)
            maps[el] = right

        return gbl_max


string = "abcabcbb"
s = Solution()
ans = s.lengthOfLongestSubstring(string)
print(ans)
