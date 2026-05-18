class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # for each number i, see if there is a j that exists... can you look at just the numbers after j? 
        
        # for i in range(len(nums)):
        #     for j in range (i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # more optimal. put target in hashmap. return if found? 

        target_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if target_map.get(complement) != None:
                return [target_map.get(complement), i]
            else:
                target_map[nums[i]] = i
        