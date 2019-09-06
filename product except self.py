from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #return list(reduce(lambda x,y: x*y, a[:i]+a[i+1:]) for i in range(len(a)))
        res = [1] * len(nums)
        lc, rc = 1,1
        for i in range(len(nums)):
            res[i] *= lc
            res[-i-1] *= rc
            lc *= nums[i]
            rc *= nums[-i-1]
        
        return res