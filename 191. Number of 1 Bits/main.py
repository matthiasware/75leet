class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        hw = 0
        for bit in n:
            if bit == '1':
                hw += 1
        return hw


# more ellegant with same complexity
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n & (n - 1)
            res += 1
        return res
