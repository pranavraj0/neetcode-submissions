class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # or to eliminate cols start of each col? no i don't think thats efficient... but let me analyze

        lRow = 0
        rRow = len(matrix) - 1

        

        while lRow <= rRow:
            mRow = (lRow + rRow) // 2
            print(lRow, mRow, rRow)

            lCol = 0
            rCol = len(matrix[mRow]) - 1

            while lCol <= rCol:
                mCol = (lCol + rCol) //2

                if matrix[mRow][mCol] < target:
                    lCol = mCol + 1
                elif matrix[mRow][mCol] > target:
                    rCol = mCol - 1
                else:
                    return True
            if lCol == 0:
                rRow = mRow - 1
            elif lCol == len(matrix[mRow]):
                lRow = mRow + 1
            else: #the case the lcol and rcol are within mrow but the target doesn't exist within the row  
                print(lCol, rCol)
                return False
        return False




        
