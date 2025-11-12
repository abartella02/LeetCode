"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and
change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing
the above operations.
"""


class Solution:
    """
    Use sliding window

    If occurrences of most frequent character in the range (right, left) and window
    size (right - left + 1) are different, that means there are entries in (right, left) that
    are not the same as the rest. Lets say there are j of these mismatched entries.

    If j <= k, thats fine because we can 'replace' those entries at most k times.

    If j > k, that's not good because now our range (right, left) is invalid.
        So, move left over one until either the most frequent character changes, or j <= k.
    """

    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq_map = {i: 0 for i in s}
        right, left = 0, 0
        max_len = 0
        most_freq_char_occurrences = 0

        while right < n:
            freq_map[s[right]] += 1
            most_freq_char_occurrences = max(
                most_freq_char_occurrences, freq_map[s[right]]
            )

            window_size = right - left + 1
            if window_size - most_freq_char_occurrences > k:
                # then there are more than k mistakes in the range we selected
                freq_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, window_size)
            right += 1

        return max_len
