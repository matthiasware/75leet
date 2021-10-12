# solution 1: brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx0 in range(len(nums)):
            for idx1 in range(idx0 + 1, len(nums)):
                if nums[idx0] + nums[idx1] == target:
                    return [idx0, idx1]

# solution 2: smart ;)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx1, elem1 in enumerate(nums):
            diff = target - elem1
            if diff in hashmap:
                return idx1, hashmap[diff]
            hashmap[elem1] = idx1
