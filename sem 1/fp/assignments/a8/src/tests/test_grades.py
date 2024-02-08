from unittest import TestCase
from src.domain.grade import Grade
from src.repository.memory_repository import MemoryRepository, RepositoryIterator, RepositoryException
from src.services.grade_services import GradeServices


class TestGrade(TestCase):
    def setUp(self):
        self.repo = MemoryRepository()
        self.serv = GradeServices(self.repo)
        self.__grades = {(2001, 1008): Grade(1008, 2001, 10),
                         (2002, 1007): Grade(1007, 2002),
                         (2007, 1003): Grade(1003, 2007, 7)}

    def test_grade_domain(self):
        self.assertEqual(self.__grades[(2001, 1008)].student_id, 1008)
        self.assertEqual(self.__grades[(2002, 1007)].assignment_id, 2002)
        self.assertEqual(self.__grades[(2007, 1003)].grade, 7)

        new = Grade(1003, 2007)
        new.grade = 7
        self.assertEqual(new, self.__grades[(2007, 1003)])
        self.assertEqual(str(Grade(1003, 2007, 7)), str(self.__grades[(2007, 1003)]))

    def test_get_grade(self):
        self.assertEqual(self.repo.grades(), self.repo.grades())
        self.assertEqual(self.repo.get_by_id_grades((2001, 1001)), self.repo.get_by_id_grades((2001, 1001)))

    def test_assign_to_student(self):
        self.repo.assign_to_student(2001, 1001)
        self.repo.grade_student(2001, 1001, 10)
        self.assertEqual(self.repo.get_by_id_grades((2001, 1001)).grade, 10)

    def test_grade_instantiation(self):
        grade_instance = Grade(1003, 2007, 7)
        self.assertEqual(grade_instance.assignment_id, 2007)
        self.assertEqual(grade_instance.student_id, 1003)
        self.assertEqual(grade_instance.grade, 7)

    def test_grade_equality(self):
        grade_instance1 = Grade(2008, 1003, 10)
        grade_instance2 = Grade(2008, 1003, 10)
        self.assertEqual(grade_instance1, grade_instance2)

    def test_grade_inequality_due_to_grade_value(self):
        grade_instance1 = Grade(2008, 1003, 8)
        grade_instance2 = Grade(2008, 1003, 9)
        self.assertNotEqual(grade_instance1, grade_instance2)

    def test_grade_inequality_due_to_assignment(self):
        grade_instance1 = Grade(2008, 1003, 8)
        grade_instance2 = Grade(2003, 1003,8)
        self.assertNotEqual(grade_instance1, grade_instance2)

    def test_grade_inequality_due_to_student(self):
        grade_instance1 = Grade(2008, 1003, 8)
        grade_instance2 = Grade(2008, 1004, 8)
        self.assertNotEqual(grade_instance1, grade_instance2)

    def test_remove_grades_by_assignment_and_others(self):
        try:
            self.repo.remove_grades_by_assignment(2001)
            self.repo.assignments_by_student_id(1001)
            self.repo.students_received_assignment(2001)
            self.repo.students_received_assignment(2002)
            self.repo.students_received_assignment(2003)
            self.repo.late_students()
            self.repo.best_performance_students()
            assert True
        except Exception:
            assert False

    def test_iterator_creation(self):
        data = [1, 2, 3]
        iterator = RepositoryIterator(data)
        self.assertEqual(iterator._RepositoryIterator__data, data)
        self.assertEqual(iterator._RepositoryIterator__pos, -1)

    def test_next_method(self):
        data = [1, 2, 3]
        iterator = RepositoryIterator(data)

        result = iterator.__next__()
        self.assertEqual(result, 1)
        self.assertEqual(iterator._RepositoryIterator__pos, 0)

        result = iterator.__next__()
        self.assertEqual(result, 2)
        self.assertEqual(iterator._RepositoryIterator__pos, 1)

        result = iterator.__next__()
        self.assertEqual(result, 3)
        self.assertEqual(iterator._RepositoryIterator__pos, 2)

        with self.assertRaises(StopIteration):
            iterator.__next__()

    def test_grades_services(self):
        self.serv.assign_to_student(2001, [1001])
        self.assertIsNotNone(self.repo.get_by_id_grades((2001, 1001)))
        self.assertIsNone(self.serv.assignments_by_student_id(1001))
        with self.assertRaises(RepositoryException):
            self.serv.assign_to_student(20023, [1001])
        with self.assertRaises(RepositoryException):
            self.serv.assign_to_student(2002, [10013])
        self.serv.grade_student(2001, 1001, 10)
        self.assertEqual(self.repo.get_by_id_grades((2001, 1001)).grade, 10)