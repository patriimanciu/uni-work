from collections import defaultdict
from datetime import date
from random import choice, randint

from src.domain.assignment import Assignment, generate_assignments
from src.domain.grade import Grade
from src.domain.student import Student, generate_students


class RepositoryException(Exception):
    pass


class RepositoryIterator:
    def __init__(self, data: list):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if self.__pos == len(self.__data):
            raise StopIteration()
        return self.__data[self.__pos]


class MemoryRepository:
    # add, remove, update, and list both students and assignments
    def __init__(self):
        # key is the object ID
        self.__students = self.initial_students(generate_students(20))
        self.__assignments = self.initial_assignments(generate_assignments(20))
        self.__grades = self.randomly_assign_assignments(25)

    # general getters / setters

    def grades(self):
        return self.__grades

    def get_by_id_grades(self, _id: tuple):
        return self.__grades.get(_id, None)

    def assignment(self):
        return self.__assignments

    def students(self):
        return self.__students

    # Students functionalities

    def initial_students(self, new: dict) -> dict:
        """
        Initializes the self.__students field with a dict from the new parameter
        :param new:
        :return:
        """
        self.__students = new.copy()
        return self.__students

    def get_by_id_students(self, _id):
        """
        Returns a student if the ID is found or None otherwise
        :param _id:
        :return:
        """
        return self.__students.get(_id, None)

    def add_students(self, stud: Student):
        """
        Adds a student to the list
        :param stud: new student to be added
        :return:
        """
        if self.get_by_id_students(stud.id):
            raise RepositoryException("There's already a student with this ID.")
        _id = stud.id
        self.__students[_id] = stud

    def remove_students(self, _id):
        """
        Removes a student from dictionary by a given ID, which is the KEY in the dict
        :param _id:
        :return:
        """
        if self.get_by_id_students(_id) is None:
            raise RepositoryException("A student with this ID doesn't exist.")
        student = self.__students.pop(_id)
        self.remove_grades_by_student(student.id)

    def remove_grades_by_student(self, _id):
        grades_to_remove = [key for key in self.__grades if key[1] == _id]
        for key in grades_to_remove:
            self.__grades.pop(key)

    def update_students(self, student: Student):
        """
        Changes the name and group of a given student
        :param student: to be updated
        :return:
        """
        if self.get_by_id_students(student.id) is None:
            raise RepositoryException("A student with this ID doesn't exist.")
        self.__students[student.id].name = student.name
        self.__students[student.id].group = student.group

    def list_students(self):
        """
        Print all students in self.__students
        :return:
        """
        for student_id, student_instance in self.__students.items():
            print(f"Student ID: {student_instance.id}, Name: {student_instance.name}, Group: {student_instance.group}")

    # Assignments

    def initial_assignments(self, new: dict) -> dict:
        """
        Initializes assignments
        :param new:
        :return:
        """
        self.__assignments = new.copy()
        return self.__assignments

    def get_by_id_assignments(self, _id):
        """
        Returns an assignment by a given ID
        :param _id:
        :return:
        """
        return self.__assignments.get(_id, None)

    def add_assignments(self, assignment: Assignment):
        """
        Adds an assignment, the parameter, to the current dict self.__assignments
        :param assignment:
        :return:
        """
        if self.get_by_id_assignments(assignment.id):
            raise RepositoryException("There's already an assignment with this ID.")
        self.__assignments[assignment.id] = assignment

    def remove_assignments(self, _id):
        """
        Removes assigment with a given ID
        :param _id:
        :return:
        """
        if self.get_by_id_assignments(_id) is None:
            raise RepositoryException("An assignment with this ID doesn't exist.")
        assignment = self.__assignments.pop(_id)
        self.remove_grades_by_assignment(assignment.id)

    def remove_grades_by_assignment(self, _id):
        grades_to_remove = [key for key in self.__grades if key[0] == _id]
        for key in grades_to_remove:
            self.__grades.pop(key)

    def update_assignments(self, assignment: Assignment):
        """
        Updates the description and deadline of a given assignment
        :param assignment:
        :return:
        """
        if self.get_by_id_assignments(assignment.id) is None:
            raise RepositoryException("An assignment with this ID doesn't exist.")
        self.__assignments[assignment.id].description = assignment.description
        self.__assignments[assignment.id].deadline = assignment.deadline

    def list_assignments(self):
        """
        Prints all current assignments
        :return:
        """
        for assignment_id, assignment_instance in self.__assignments.items():
            print(f"Assignment ID: {assignment_instance.id} | Description: {assignment_instance.description}, Deadline: {assignment_instance.deadline}")

    # GRADES

    def list_grades(self):
        for grade_key, grade_instance in self.__grades.items():
            assignment_id, student_id = grade_key
            print(f"Assignment ID: {assignment_id}, Student ID: {student_id} -> Grade: {grade_instance.grade}")

    def assign_to_student(self, assignment_id: int, student_id: int):
        student = None
        for stud_id, stud in self.__students.items():
            if stud_id == student_id:
                student = stud
                break

        assignment = None
        for assign_id, assign in self.__assignments.items():
            if assign_id == assignment_id:
                assignment = assign
                break

        if student and assignment:
            grade_key = (assignment.id, student.id)
            if grade_key not in self.__grades:
                self.__grades[grade_key] = Grade(assignment, student)

    def assignments_by_student_id(self, student_id: int):
        student_assignments = {}
        for (assignment_id, current_student_id), grade_instance in self.__grades.items():
            if current_student_id == student_id:
                student_assignments[(assignment_id, current_student_id)] = self.get_by_id_grades((assignment_id, current_student_id))
        # print(student_assignments)
        return student_assignments

    def randomly_assign_assignments(self, n: int) -> dict:
        grades = {}
        students = list(self.__students.values())
        assignments = list(self.__assignments.values())

        for i in range(n):
            assign = choice(assignments)
            stud = choice(students)
            grade_key = (assign.id, stud.id)

            if grade_key not in grades:
                arg = randint(1, 2)
                # 1 represents None and 2 represent an actual grade
                if arg == 1:
                    grades[grade_key] = Grade(assign, stud)
                elif arg == 2:
                    grades[grade_key] = Grade(assign, stud, randint(2, 10))

            else:
                i -= 1
        self.__grades = grades
        return grades

    def grade_student(self, assignment_id, student_id, grade_value):
        assignment_key = (assignment_id, student_id)
        existing_grade = self.get_by_id_grades(assignment_key)

        if existing_grade and existing_grade.grade is None:
            assignment = self.get_by_id_assignments(assignment_id)
            student = self.get_by_id_students(student_id)

            if assignment and student:
                grade_instance = Grade(assignment, student, grade_value)
                self.grades()[assignment_key] = grade_instance
            else:
                raise RepositoryException("The assignment was not found")
        else:
            raise RepositoryException("The grade already exists")

    # STATISTICS

    def students_received_assignment(self, assignment_id: int) -> list:
        students = []
        students_none = []
        for (current_assignment_id, student_id), grade_instance in self.__grades.items():
            if current_assignment_id == assignment_id:
                if grade_instance.grade is not None:
                    students.append((student_id, grade_instance.grade))
                else:
                    students_none.append((student_id, grade_instance.grade))
        students.sort(key=lambda x: x[1], reverse=True)

        return students + students_none

    def late_students(self) -> list:
        today = date.today()
        late_stud = []
        for (assignment_id, student_id), grade_instance in self.__grades.items():
            assignment = self.get_by_id_assignments(assignment_id)
            if assignment and assignment.deadline < today and grade_instance.grade is None and student_id not in late_stud:
                late_stud.append(student_id)
        return late_stud

    def best_performance_students(self) -> list:
        student_grades = defaultdict(list)
        for (assignment_id, student_id), grade_instance in self.__grades.items():
            if grade_instance.grade is not None:
                student_grades[student_id].append(grade_instance.grade)
        average_grade = {}
        for student_id, grades in student_grades.items():
            average_grade[student_id] = sum(grades) / len(grades)

        sorted_students = sorted(average_grade.items(), key=lambda x: x[1], reverse=True)
        return sorted_students
