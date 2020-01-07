class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i, ss in enumerate(s):
            for c in s[i+1:]:
                if c in ss:
                    break
                else:
                    ss += c
            longest = max(longest, len(ss))

        return longest
