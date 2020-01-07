class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                return digits
            else:
                temp_sum = digits[i] + carry

                carry = temp_sum // 10
                digits[i] = temp_sum % 10

        if carry > 0:
            digits.insert(0, carry)

        return digits
