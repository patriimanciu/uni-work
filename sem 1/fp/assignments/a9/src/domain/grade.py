from src.domain.assignment import Assignment
from src.domain.student import Student


class Grade:
    def __init__(self, assignment: Assignment, student: Student, grade_value: int = None):
        self.__student_id = student.id
        self.__assignment_id = assignment.id
        self.__grade_value = grade_value

    @property
    def student_id(self):
        return self.__student_id

    @property
    def assignment_id(self):
        return self.__assignment_id

    @property
    def grade(self):
        return self.__grade_value

    @grade.setter
    def grade(self, new_grade: int):
        self.__grade_value = new_grade

    def __str__(self):
        return f"Assignment ID: {self.assignment_id}, Student ID: {self.student_id} -> Grade: {self.grade}"

    def __eq__(self, other):
        if isinstance(other, Grade):
            return (
                    self.student_id == other.student_id and
                    self.assignment_id == other.assignment_id and
                    self.grade == other.grade
            )
        return False
