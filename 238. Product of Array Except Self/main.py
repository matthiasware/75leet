class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_lst = [1]
        prefix_lst = [1]
        #
        for num in nums[:-1]:
            suffix_lst.append(suffix_lst[-1] * num)
        for num in nums[::-1][:-1]:
            prefix_lst.append(prefix_lst[-1] * num)
        
        return [s * p for s,p in zip(suffix_lst, prefix_lst[::-1])]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]
        for idx in range(n - 1):
            output.append(output[-1] * nums[idx])
        postfix = 1
        for idx in range(n - 2, -1, -1):
            postfix *= nums[idx + 1]
            output[idx] *= postfix
        return output
