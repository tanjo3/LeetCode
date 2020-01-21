class Solution:
    def countAndSay(self, n: int) -> str:
        old_string = "1"

        for _ in range(1, n):
            new_string = ""

            prev_c = old_string[0]
            count = 1

            for c in old_string[1:]:
                if c != prev_c:
                    new_string += str(count) + prev_c
                    prev_c = c
                    count = 1
                else:
                    count += 1

            new_string += str(count) + prev_c
            old_string = new_string

        return old_string
