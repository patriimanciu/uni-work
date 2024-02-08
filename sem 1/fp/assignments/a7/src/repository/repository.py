from src.domain.domain import Student
from src.services.services import Services
import pickle


class RepositoryError(Exception):
    pass


class MemoryRepository:
    def __init__(self):
        self.__changes = []
        self.__students = []

    @property
    def students(self):
        return self.__students

    @property
    def changes(self):
        return self.__changes

    @students.setter
    def students(self, new_stud: Student):
        self.__students = new_stud

    @changes.setter
    def changes(self, value):
        self.__changes = value

    def add_student_initial(self, student: Student):
        """
        Add the initial students, called only if the file is empty, without adding it to "changes" because these cannot be undone
        :param student: the new student to be added
        :return:
        """
        if student in self.__students:
            raise ValueError("There's already a student with this ID.")
        self.__students.append(student)

    def add_student(self, student: Student):
        """
        Add students and saves the list of students before appending it to the final list
        :param student: new student to be added
        :return:
        """
        if student in self.__students:
            raise ValueError("There's already a student with this ID.")
        self._save_history()
        self.__students.append(student)

    def display_students(self):
        for student in self.__students:
            print(f"ID: {student.id}, Name: {student.name}, Group: {student.group}")

    def filter_students(self, group):
        self._save_history()
        filtered_students = []
        for student in self.__students:
            if student.group == group:
                filtered_students.append(student)
        self.__students = filtered_students

    def _save_history(self):
        """
        Adds to the __changes parameter a copy of the __students list
        :return:
        """
        self.__changes.append(self.__students.copy())

    def undo(self):
        if len(self.__changes) == 0:
            raise ValueError("Nothing to undo!")
        self.__students = self.__changes.pop()


class TextFileRepository(MemoryRepository):
    def __init__(self, path_file):
        super().__init__()
        self.__path_file = path_file

    def filename(self):
        return self.__path_file

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for student in self.students:
                    file.write(f"{student.id},{student.name},{student.group}\n")
        except Exception as err:
            raise RepositoryError(f"Error saving to file: {err}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                if file.readable() and len(file.read()) == 0:
                    raise RepositoryError("File is empty.")
                file.seek(0)
                for line in file:
                    student_data = line.strip().split(',')
                    student = Student(int(student_data[0]), student_data[1], int(student_data[2]))
                    self.add_student(student)
        except FileNotFoundError as e:
            raise RepositoryError(f"Error loading from file: {e}")


class BinaryFileRepository(MemoryRepository):
    def __init__(self, path_file):
        super().__init__()
        self.__path_file = path_file

    def filename(self):
        return self.__path_file

    def save_to_file(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.students, file)
        except Exception as err:
            raise RepositoryError(f"Error saving to file: {err}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                if file.readable() and len(file.read()) == 0:
                    raise RepositoryError("File is empty.")
                file.seek(0)
                self.students = pickle.load(file)
        except (pickle.UnpicklingError, FileNotFoundError) as err:
            raise RepositoryError(f"Error loading from file: {err}")
