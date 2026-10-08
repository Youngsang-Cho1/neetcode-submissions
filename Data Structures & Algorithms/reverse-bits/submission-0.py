class Solution:
    def reverseBits(self, n: int) -> int:

        bin_n = bin(n)[2:]
        zeros = 32 - len(bin_n)
        res = bin_n[::-1] + '0' * zeros
        return int(res, 2)
        