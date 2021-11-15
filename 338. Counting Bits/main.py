# Brute force ;)

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for num in range(1, n+1, 1):
            hw = 0
            while num > 0:
                num = num & (num - 1)
                hw += 1
            res.append(hw)
        return res


# really fast solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        while len(res) < (n+1):
            res += [num + 1 for num in res]
        return res[:n+1]