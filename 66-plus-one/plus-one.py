class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = len(digits) - 1
        carry = 1
        while r >= 0:
            s = digits[r] + carry
            digits[r] = s % 10
            carry = s // 10
            r -= 1
        if carry:
            return [carry] + digits
        return digits