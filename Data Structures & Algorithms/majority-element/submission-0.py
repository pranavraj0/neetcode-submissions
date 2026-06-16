class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) //2

        #only 1 majority element... could put all in hashmap potentially

        #sort list and check each section also works... 

        frequency_map = {}

        for n in nums:
            frequency_map[n] = frequency_map.get(n, 0) + 1

        for key in frequency_map:
            if frequency_map[key] >= majority:
                return key
        