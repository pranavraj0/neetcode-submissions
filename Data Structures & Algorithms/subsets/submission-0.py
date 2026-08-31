class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSubsets = [[]]
        for i in nums:
            for j in range(len(currSubsets)):
                cLen = len(currSubsets[j])
                # append or don't append... 
                currSubsets[j].append(i)
                currSubsets.append(currSubsets[j][:cLen])

        print(currSubsets)
        return currSubsets




        
        
        