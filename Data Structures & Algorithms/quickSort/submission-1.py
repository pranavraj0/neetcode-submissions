# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortRec(pairs, 0, len(pairs))
    def quickSortRec(self, pairs, l, r):
        print(l, r)
        # if l = r, empty array... that is the worst case anyway, won't be worse than that
        # or if 
        if r - l <= 1:
            return pairs
        pivot = pairs[r - 1]

        swap = l
        for i in range(l, r - 1): # can do r or r - 1, pivot won't be swapped in loop either way and can swap at end
            if pairs[i].key < pivot.key:
                # swap with position to swap
                tmp = pairs[swap]
                pairs[swap] = pairs[i]
                pairs[i] = tmp
                swap +=1
        
        tmp = pairs[swap]
        pairs[swap] = pairs[r - 1]
        pairs[r - 1] = tmp

        self.quickSortRec(pairs, l, swap)
        self.quickSortRec(pairs, swap + 1, r)
        return pairs

        
    
        