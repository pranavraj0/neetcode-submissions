class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # how to make more efficient. start from the end? 
        currentMax = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            nextMax = max(currentMax, arr[i])
            arr[i] = currentMax
            currentMax = nextMax
            
        arr[-1] = -1
        return arr

        