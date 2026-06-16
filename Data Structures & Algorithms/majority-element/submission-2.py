class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res, count = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == res:
                count+=1
            elif count > 1 and nums[i] != res:
                count-=1
            else:
                res = nums[i]
        return res