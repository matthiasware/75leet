# brute force solution

class Solution_BF:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set([])
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    t = (nums[i], nums[j], nums[k])
                    if sum(t) == 0 and t not in res:
                            res.add(t)
        return res

# speed up by reducing problem to two sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set([])
        nums = sorted(nums)
        #
        for i in range(n):
            diff = {}
            a = nums[i]
            for j in range(i + 1, n):
                b = nums[j]
                d = 0 - (a + b)
                diff[d] = (i, j)
            for k in range(i + 1,n):
                c = nums[k]
                if c in diff:
                    i, j = diff[c]
                    if i != j and j != k and i != k:
                        res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return res
                    

# WITH POINTERA, QUITE FAST
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            # dont reuse same value twice
            if i > 0 and nums[i - 1] == a:
                continue
            
            # solve two sums
            l = i + 1
            r = n - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r = r - 1
                elif threesum < 0:
                    l = l + 1
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    # update pointers
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l +=1
        return res