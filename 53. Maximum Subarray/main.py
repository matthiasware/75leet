class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum