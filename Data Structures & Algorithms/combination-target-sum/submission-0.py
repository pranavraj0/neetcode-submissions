class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        def dfs(i, currentSum):
            if i == len(nums):
                return
            if currentSum == target:
                res.append(combo.copy())
                return
            elif currentSum > target:
                return

            # can choose any in nums? 
            # what decision do you make at current - to include or not? no... but you can include multiple times... 

            # assumes currentSum < targetSum



            currentSum += nums[i] # that assumes you include the current... 
            
            combo.append(nums[i])
            dfs(i, currentSum)

            combo.pop()
            currentSum -= nums[i]
            dfs(i + 1, currentSum)
            

        dfs(0, 0)
        return res