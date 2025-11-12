class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        letters = len(needle)
        for i in range(0, len(haystack) - letters + 1):
            if haystack[i : i + letters] == needle:
                return i
        return -1


needle = "a"
haystack = "a"
sol = Solution()
print(sol.strStr(haystack, needle))
