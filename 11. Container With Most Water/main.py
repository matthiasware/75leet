# brute force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for w1, h1 in enumerate(height):
            for w2, h2 in enumerate(height):
                a = min(h1, h2) * (w2 - w1)
                res = max(res, a)
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l <= r:
            hl = height[l]
            hr = height[r]
            a = min(hl, hr) * (r - l)
            res = max(res, a)
            if hl <= hr:
                l += 1
            else:
                r -= 1
        return res