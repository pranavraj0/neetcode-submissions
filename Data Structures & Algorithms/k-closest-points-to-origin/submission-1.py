class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSelect(points, k - 1, 0, len(points) - 1)
        return points[0:k]

    def quickSelect(self, points, rank, l, r):
        if r - l + 1 <= 1:
            return

        pivot = points[r]
        pivot_dist = pivot[0]**2 + pivot[1]**2
        swap = l

        for i in range(l, r):
            if points[i][0]**2 + points[i][1]**2 < pivot_dist:
                tmp = points[swap]
                points[swap] = points[i]
                points[i] = tmp
                swap +=1 #guaranteed all to the left of swap are less than pivot

        points[r] = points[swap]
        points[swap] = pivot

        if swap < rank:
            self.quickSelect(points, rank, swap + 1, r)
        elif swap > rank:
            self.quickSelect(points, rank, l, swap - 1)
        if swap == rank:
            return
        
            
        
