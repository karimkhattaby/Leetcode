class Solution:
    def reverseBits(self, n: int) -> int:
        binum = list(bin(n)[2:])
        lst = ['0'] * (32-len(binum))
        lst.extend(binum)
        return int(''.join(reversed(lst)),2)