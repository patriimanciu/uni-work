import pickle
import os

from datetime import date
from random import choice, randint

from src.domain.assignment import Assignment, generate_assignments
from src.domain.grade import Grade
from src.domain.student import Student, generate_students
from src.repository.memory_repo import MemoryRepository, RepositoryException


class BinaryFileRepository(MemoryRepository):
    def __init__(self, path_files):
        super().__init__()
        self.__path_file = path_files
        self.__initial_random_stud = generate_students(20)
        self.__initial_random_assign = generate_assignments(20)
        self.__initial_random_grades = {}
        self.__load_from_file_students()
        self.__load_from_file_assignments()
        self.__load_from_file_grades()

    def get_students_path(self):
        return self.__path_file["students"]

    def get_assignments_path(self):
        return self.__path_file["assignments"]

    def get_grades_path(self):
        return self.__path_file["grades"]

        # Overwriting student methods

    def add_students(self, stud: Student):
        super().add_students(stud)
        self.__save_to_file_students()

    def remove_students(self, _id):
        super().remove_students(_id)
        self.__save_to_file_students()

    def update_students(self, student: Student):
        super().update_students(student)
        self.__save_to_file_students()

        # Overwriting assignments methods

    def add_assignments(self, assignment: Assignment):
        super().add_assignments(assignment)
        self.__save_to_file_assignments()

    def remove_assignments(self, _id):
        super().remove_assignments(_id)
        self.__save_to_file_assignments()

    def update_assignments(self, assignment: Assignment):
        super().update_assignments(assignment)
        self.__save_to_file_assignments()

        # Overwriting grade methods

    def assign_to_student(self, assignment_id: int, student_id: int):
        super().assign_to_student(assignment_id, student_id)
        self.__save_to_file_grades()

    def grade_student(self, assignment_id, student_id, grade_value):
        super().grade_student(assignment_id, student_id, grade_value)
        self.__save_to_file_grades()

    def __save_to_file_students(self, filename=None):
        try:
            if filename is None:
                filename = self.get_students_path()
            with open(filename, "wb") as file:
                for students in self.students():
                    pickle.dump(self.get_by_id_students(students), file)
        except Exception as err:
            raise RepositoryException(f"Error saving to file: {err}")

    def __save_to_file_assignments(self, filename=None):
        try:
            if filename is None:
                filename = self.get_assignments_path()
            with open(filename, "wb") as file:
                for assignment in self.assignment():
                    # print(assignment)
                    pickle.dump(self.get_by_id_assignments(assignment), file)
        except Exception as err:
            raise RepositoryException(f"Error saving to file: {err}")

    def __save_to_file_grades(self, filename=None):
        try:
            if filename is None:
                filename = self.get_grades_path()
            with open(filename, "wb") as file:
                for grd in self.grades():
                    # print(grd)
                    pickle.dump(self.get_by_id_grades(grd), file)
        except Exception as err:
            raise RepositoryException(f"Error saving to file: {err}")

    def __load_from_file_students(self, filename=None):
        if filename is None:
            filename = self.get_students_path()
        with open(filename, "rb") as file:
            if not os.path.exists(filename) or os.path.getsize(filename) == 0:
                self.students_setter(self.__initial_random_stud)
                return
            try:
                while True:
                    stud = pickle.load(file)
                    # print(stud)
                    self.add_students(stud)
            except EOFError:
                pass

    def __load_from_file_assignments(self, filename=None):
        if filename is None:
            filename = self.get_assignments_path()
        with open(filename, "rb") as file:
            if not os.path.exists(filename) or os.path.getsize(filename) == 0:
                self.assignments_setter(self.__initial_random_assign)
                return
            try:
                while True:
                    assign = pickle.load(file)
                    # print(assign)
                    self.add_assignments(assign)

            except EOFError:
                pass

    def __load_from_file_grades(self, filename=None):
        if filename is None:
            filename = self.get_grades_path()
        with open(filename, "rb") as file:
            if not os.path.exists(filename) or os.path.getsize(filename) == 0:
                self.grades_setter(self.randomly_assign_assignments(20))
                # print(self.__initial_random_grades)
                return
            try:
                while True:
                    grd = pickle.load(file)
                    # print(grd)
                    self.assign_to_student(grd.assignment_id, grd.student_id)
                    if grd.grade is not None:
                        self.grade_student(grd.assignment_id, grd.student_id, grd.grade)

            except EOFError:
                pass

    def save_data_binary(self):
        self.__save_to_file_students()
        self.__save_to_file_assignments()
        self.__save_to_file_grades()

    def randomly_assign_assignments(self, n: int):
        grades = {}
        students = list(self.__initial_random_stud.values())
        assignments = list(self.__initial_random_assign.values())

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
        self.__initial_random_grades = grades
        return grades
