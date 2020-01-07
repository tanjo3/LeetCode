class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        n = min([len(s) for s in strs])
        lcp = ""

        for i in range(n):
            if all([s[i] == strs[0][i] for s in strs]):
                lcp += strs[0][i]
            else:
                break

        return lcp
