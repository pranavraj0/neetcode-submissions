class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1, n2, merged = m - 1, n-1, m + n - 1

        while n1 >=0 and n2 >=0:
            
            if nums1[n1] > nums2[n2]:
                nums1[merged] = nums1[n1]
                n1-=1
                
            else:
                nums1[merged] = nums2[n2]
                n2-=1
            merged -=1

            print(n1, n2, merged)
        if n2 >=0:
            for i in range(n2 + 1):
                nums1[i] = nums2[i]
