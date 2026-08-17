class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsZero = 0
        studentsOne = 0

        for s in students:
            if s == 0:
                studentsZero +=1
            if s == 1:
                studentsOne +=1

        for s in sandwiches:
            if s == 0:
                if studentsZero > 0:
                    studentsZero -=1
                else:
                    return studentsOne
            if s == 1:
                if studentsOne > 0:
                    studentsOne -=1
                else:
                    return studentsZero

        return 0