# Non binary solutions
# actually this is too complicated and can be simplified!
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_act = 0
        nums_max = 0
        nums_min = 10**4
        for num in nums:
            nums_min = min(nums_min, num)
            nums_max = max(nums_max, num)
            sum_act += num
        sum_exp = (nums_max * (nums_max + 1)) // 2
        if sum_act == sum_exp:
            if nums_min == 0:
                res = nums_max + 1
            else:
                res = 0
        elif sum_exp > sum_act:
            res = sum_exp - sum_act
        return res

# Binary solution that is quite ellegant
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for idx, num in enumerate(nums):
            res = res ^ idx
            res = res ^ num
        res = res ^ (idx + 1)
        return res