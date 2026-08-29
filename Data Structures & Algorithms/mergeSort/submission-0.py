# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def mergeSortRec(l, r):
            print(l, r)
            if l == r:
                return
            
            m = (r + l) // 2 # floor

            if l <=r:
                mergeSortRec(l, m)
                mergeSortRec(m + 1, r)
                merge(l, m, r)

        def merge(l, m, r):

            # merge l to m and m+ 1 to r

            temp = [0] * (r - l + 1)

            i = 0
            left = l
            middle = m + 1
            while left < m + 1 and middle < r + 1:
                if pairs[left].key <= pairs[middle].key:
                    temp[i] = pairs[left]
                    left +=1
                else:
                    temp[i] = pairs[middle]
                    middle +=1
                i +=1
            
            while left < m + 1:
                temp[i] = pairs[left]
                left +=1
                i +=1
            while middle < r + 1:
                temp[i] = pairs[middle]
                middle +=1
                i +=1
            
            for i in range(len(temp)):
                pairs[i + l] = temp[i]

        mergeSortRec(0, len(pairs) - 1)
        return pairs



