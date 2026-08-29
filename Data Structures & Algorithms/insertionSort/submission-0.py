# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        to_return = []
        for i in range(0, len(pairs)):
            r = []
            for j in range(i, 0, -1):
                print(j, pairs[j].key, pairs[j-1].key)
                if pairs[j].key < pairs[j - 1].key:
                    tmp = pairs[j-1]
                    pairs[j-1] = pairs[j]
                    pairs[j] = tmp
            for p in pairs:
                r.append(p)
            to_return.append(r)
                

        return to_return
        