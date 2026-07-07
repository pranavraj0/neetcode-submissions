class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # position to fill
        # position of next unique element
        # how can I use 2 pointers with o(n) runtime? 
        # track last element of previous unique element
        if len(nums) == 0:
            return 0

        unique = 0
        toFill = 1
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[unique]:
                nums[toFill] = nums[i]
                toFill +=1
                unique = i
                k+=1
        return k


            



             


