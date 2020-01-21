import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = re.sub(r"[\W_]+", "", s.lower())
        return stripped == stripped[::-1]
