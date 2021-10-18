# Brute Force

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p_max = -10
        for idx_offset in range(len(nums)):
            p_cur = 1
            for idx in range(idx_offset, len(nums)):
                p_cur *= nums[idx]
                p_max = max(p_max, p_cur)
        return p_max


# all positive -> incrasing
# with negatives, it depends on number of negatives
# require even number of negatives
# edge case: zeros will split the array into subarrays without zeros
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_max = nums[0]
        c_min = nums[0]
        p_max = nums[0]
        for num in nums[1:]:
            if num == 0:
                c_max = 1
                c_min = 1
                p_max = max(num, p_max)
            else:
                a = c_max * num
                b = c_min * num
                c_max = max(a, b, num)
                c_min = min(a, b, num)
                #
                p_max = max(c_max, p_max)
        return p_max


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cMin, cMax = 1, 1
        for n in nums:
            if n == 0:
                cMin, cMax = 1, 1
                continue
            cMin, cMax = min(n * cMax, n * cMin, n), max(n * cMax, n * cMin, n)
            res = max(res, cMax)
        return res