from datetime import date
from random import choice, randint

from src.domain.assignment import Assignment, generate_assignments
from src.domain.grade import Grade
from src.domain.student import Student, generate_students
from src.repository.memory_repo import MemoryRepository, RepositoryException


class TextFileRepository(MemoryRepository):
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

    def __save_to_file_students(self, filename=None):
        try:
            if filename is None:
                filename = self.get_students_path()
            with open(filename, 'w') as file:
                for student in self.students():
                    stud = self.get_by_id_students(student)
                    file.write(f"{stud.id},{stud.name},{stud.group}\n")
        except Exception as err:
            raise RepositoryException(f"Error saving to file: {err}")

    def __save_to_file_assignments(self, filename=None):
        try:
            if filename is None:
                filename = self.get_assignments_path()
            with open(filename, 'w') as file:
                for assign in self.assignment():
                    assign_instance = self.get_by_id_assignments(assign)
                    file.write(f"{assign_instance.id},{assign_instance.description},{assign_instance.deadline.year},{assign_instance.deadline.month},{assign_instance.deadline.day}\n")
        except Exception as err:
            raise RepositoryException(f"Error saving to file: {err}")

    def __save_to_file_grades(self, filename=None):
        try:
            if filename is None:
                filename = self.get_grades_path()
            with open(filename, 'w') as file:
                for grade_instance in self.grades():
                    if isinstance(self.get_by_id_grades(grade_instance).grade, int):
                        file.write(
                            f"{grade_instance[0]},{grade_instance[1]},{self.get_by_id_grades(grade_instance).grade}\n")
                    else:
                        file.write(f"{grade_instance[0]},{grade_instance[1]},-1\n")
        except Exception as err:
            raise RepositoryException(f"Error saving to file: {err}")

    def __load_from_file_students(self, filename=None):
        try:
            if filename is None:
                filename = self.get_students_path()

            with open(filename, 'r') as file:
                content = file.read()
                if content:
                    # if file.readable() and len(file.read()) == 0:
                    #     raise RepositoryException("File is empty.")
                    file.seek(0)
                    for line in file:
                        student_data = line.strip().split(',')
                        student = Student(int(student_data[0]), student_data[1], int(student_data[2]))
                        self.add_students(student)
                else:
                    self.students_setter(self.__initial_random_stud)

        except FileNotFoundError as e:
            raise RepositoryException(f"Error loading from file: {e}")

    def __load_from_file_assignments(self, filename=None):
        try:
            if filename is None:
                filename = self.get_assignments_path()
            with open(filename, 'r') as file:
                content = file.read()
                if content:
                    # if file.readable() and len(file.read()) == 0:
                    #     raise RepositoryException("File is empty.")
                    file.seek(0)
                    for line in file:
                        assignment_data = line.strip().split(',')
                        assign = Assignment(int(assignment_data[0]), assignment_data[1], date(int(assignment_data[2]), int(assignment_data[3]), int(assignment_data[4])))
                        self.add_assignments(assign)
                else:
                    self.assignments_setter(self.__initial_random_assign)

        except FileNotFoundError as e:
            raise RepositoryException(f"Error loading from file: {e}")

    def __load_from_file_grades(self, filename=None):
        try:
            if filename is None:
                filename = self.get_grades_path()
            with open(filename, 'r') as file:
                content = file.read()
                if content:
                    # if file.readable() and len(file.read()) == 0:
                    #     raise RepositoryException("File is empty.")
                    file.seek(0)
                    for line in file:
                        grade_data = line.strip().split(',')
                        self.assign_to_student(int(grade_data[0]), int(grade_data[1]))
                        if int(grade_data[2]) > -1:
                            self.grade_student(int(grade_data[0]), int(grade_data[1]), int(grade_data[2]))
                else:
                    self.grades_setter(self.randomly_assign_assignments(30))

        except FileNotFoundError as e:
            raise RepositoryException(f"Error loading from file: {e}")

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

    def save_data_text(self):
        self.__save_to_file_students()
        self.__save_to_file_assignments()
        self.__save_to_file_grades()
