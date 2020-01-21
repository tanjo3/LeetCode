class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        pascal = [[1]]

        for _ in range(1, numRows):
            prev_row = pascal[-1]
            next_row = [1]
            for i in range(1, len(prev_row)):
                next_row.append(prev_row[i - 1] + prev_row[i])
            next_row.append(1)

            pascal.append(next_row)

        return pascal
