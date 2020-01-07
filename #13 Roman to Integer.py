class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0

        for i, c in enumerate(s):
            if c == 'M':
                if i > 0 and s[i-1] == 'C':
                    num += 800
                else:
                    num += 1000
            elif c == 'D':
                if i > 0 and s[i-1] == 'C':
                    num += 300
                else:
                    num += 500
            elif c == 'C':
                if i > 0 and s[i-1] == 'X':
                    num += 80
                else:
                    num += 100
            elif c == 'L':
                if i > 0 and s[i-1] == 'X':
                    num += 30
                else:
                    num += 50
            elif c == 'X':
                if i > 0 and s[i-1] == 'I':
                    num += 8
                else:
                    num += 10
            elif c == 'V':
                if i > 0 and s[i-1] == 'I':
                    num += 3
                else:
                    num += 5
            else:
                num += 1

        return num
