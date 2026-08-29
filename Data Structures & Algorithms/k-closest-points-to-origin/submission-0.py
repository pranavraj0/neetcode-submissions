class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSort(points, 0, len(points) - 1)

        return points[0:k]

    def quickSort(self, points, l, r):
        if r - l + 1 <= 1:
            return

        pivot = points[r]
        pivot_magnitude = (pivot[0]**2 + pivot[1]**2)**.5

        swap = l

        # arrange all points less than pivot to left, and points >= to right
        # switch pivot with last swap
        for i in range(l, r):
            if (points[i][0]**2 + points[i][1]**2)**.5 < pivot_magnitude:
                tmp = points[swap]
                points[swap] = points[i]
                points[i] = tmp
                swap +=1
        points[r] = points[swap]
        points[swap] = pivot
        self.quickSort(points, l, swap - 1)
        self.quickSort(points, swap + 1, r)
    
    
        