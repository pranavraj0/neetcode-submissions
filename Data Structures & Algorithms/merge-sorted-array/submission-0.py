class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = 0, 0

        sortedArr = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sortedArr.append(nums1[i])
                i += 1
            else:
                sortedArr.append(nums2[j])
                j += 1
        while i < m:
            sortedArr.append(nums1[i])
            i+=1
        
        while j < n:
            sortedArr.append(nums2[j])
            j+=1

        for x in range(m + n):
            nums1[x] = sortedArr[x]
