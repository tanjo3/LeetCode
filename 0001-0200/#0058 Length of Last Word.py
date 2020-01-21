class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splits = s.split(" ")
        for ss in reversed(splits):
            if len(ss) != 0:
                return len(ss)

        return len(s) - len(splits) + 1
