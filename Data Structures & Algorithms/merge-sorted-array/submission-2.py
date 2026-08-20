class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        temp1 = nums1[0:m + 1]
        temp2 = nums2[0:n + 1]

        i, j, k = 0, 0, 0

        while i < m and j < n:
            if temp1[i] <= temp2[j]:
                nums1[k] = temp1[i]
                i +=1
            else:
                nums1[k] = temp2[j]
                j+=1
            k +=1

        while i < m:
            nums1[k] = temp1[i]
            i+=1
            k+=1
        while j < n:
            nums1[k] = temp2[j]
            j+=1
            k+=1
        


        