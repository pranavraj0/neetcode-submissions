class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = []
        while sandwiches:
            s.append(sandwiches.pop())

        appends = 0
        while s: # if sandwiches never gets empty, will result in infinite loop. how to terminate this? if all students aren't equal to top sandwich, must terminate... make a counter of number of appends in a row and check if it equals number of students? 
            currStudent = students.pop(0)
            if currStudent == s[-1]:
                s.pop()
                appends = 0
            else:
                students.append(currStudent)
                appends +=1
            if appends == len(students):
                return len(students)
        return 0