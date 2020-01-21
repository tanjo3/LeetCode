class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1]

        for _ in range(rowIndex):
            next_row = [1]
            for i in range(1, len(prev_row)):
                next_row.append(prev_row[i - 1] + prev_row[i])
            next_row.append(1)
            prev_row = next_row

        return prev_row
