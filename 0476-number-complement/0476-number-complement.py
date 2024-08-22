class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()

        bit_mask = (1 << bit_length) - 1

        return num ^ bit_mask