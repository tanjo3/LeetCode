class Solution:
    def convertToTitle(self, n: int) -> str:
        header = ""

        while n != 0:
            rem = (n - 1) % 26 + 1
            header += chr(rem + 64)
            n = (n - rem) // 26

        return header[::-1]
