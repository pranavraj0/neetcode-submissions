class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        lRow = 0
        rRow = len(matrix) - 1
        mRow = 0
        while lRow <= rRow:
            mRow = (lRow + rRow) // 2

            if matrix[mRow][0] > target:
                rRow = mRow - 1
            elif matrix[mRow][len(matrix[mRow]) - 1] < target:
                lRow = mRow + 1
            else:
                break # found the correct row
        print(mRow, "mRow")
        lCol = 0
        rCol = len(matrix[mRow]) - 1

        while lCol <= rCol:
            
            mCol = (lCol + rCol) // 2
            print(matrix[mRow][mCol])
            if matrix[mRow][mCol] < target:
                lCol = mCol + 1
            elif matrix[mRow][mCol] > target:
                rCol = mCol - 1
            else:
                return True
        return False
