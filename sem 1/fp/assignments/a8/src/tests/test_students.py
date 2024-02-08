from unittest import TestCase
from src.domain.student import Student
from src.repository.memory_repository import MemoryRepository, RepositoryException
from src.services.student_services import StudentServices


class TestStudent(TestCase):
    def setUp(self):
        self.repo = MemoryRepository()
        self.stud = StudentServices(self.repo)
        self.__students = {1001: Student(1001, "Alex", 912),
                           1002: Student(1002, "Kate", 913),
                           1003: Student(1003, "Jess", 917),
                           1005: Student(1005, "Luke", 914)}

    def test_add(self):
        student = Student(999, "John", 912)
        self.repo.add_students(student)
        self.assertEqual(len(self.repo.students()), 21)

    def test_add_existing_student(self):
        student = Student(1005, "Luke", 914)
        with self.assertRaises(RepositoryException):
            self.repo.add_students(student)

    def test_remove_student(self):
        student_id = 1005
        self.repo.remove_students(student_id)
        self.assertIsNone(self.repo.get_by_id_students(student_id))

    def test_remove_nonexistent_student(self):
        nonexistent_student_id = 9999
        with self.assertRaises(RepositoryException):
            self.repo.remove_students(nonexistent_student_id)

    def test_create_stud(self):
        with self.assertRaises(TypeError):
            stud = Student(123,12,2)
        with self.assertRaises(TypeError):
            stud = Student(123, "Alex", "two")

    def test_eq(self):
        stud = Student(1001, "Alex", 912)
        self.assertEqual(stud, self.__students[1001])
        self.assertNotEqual(stud, self.__students[1002])

    def test_setters(self):
        stud = Student(1001, "Jessie", 913)
        self.__students[1001].name = "Jessie"
        self.__students[1001].group = 913
        self.assertEqual(stud, self.__students[1001])

    def test_str(self):
        self.assertEqual(str(Student(1001, "Alex", 912)), str(self.__students[1001]))

    def test_update_student(self):
        stud = Student(1001, "Jessie", 913)
        self.repo.update_students(stud)
        self.assertEqual(self.repo.get_by_id_students(1001), stud)

    def test_student_services(self):
        student = Student(1030, "John", 912)
        self.stud.add(1030, "John", 912)
        self.assertEqual(len(self.repo.students()), 21)

        student = Student(1030, "Alex", 912)
        self.stud.update(1030, "Alex", 912)
        self.assertEqual(self.repo.get_by_id_students(1030), student)

        self.stud.remove(1030)
        self.assertEqual(len(self.repo.students()), 20)


