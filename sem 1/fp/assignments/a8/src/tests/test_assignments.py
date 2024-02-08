from datetime import date
from unittest import TestCase
from src.domain.assignment import Assignment
from src.repository.memory_repository import RepositoryException, MemoryRepository
from src.services.assignment_services import AssignmentServices


class TestAssignment(TestCase):
    def setUp(self):
        self.repo = MemoryRepository()
        self.assign = AssignmentServices(self.repo)
        self.__assignments = {2001: Assignment(2001, "project", date(2023, 6, 1)),
                             2002: Assignment(2002, "coding assignment", date(2023, 12, 18)),
                             2003: Assignment(2003, "coding assignment", date(2023, 2, 2)),
                             2004: Assignment(2004, "essay", date(2023, 2, 7)),
                             2006: Assignment(2006, "project", date(2023, 6, 3))}

    def test_add_and_get_assignment(self):
        assignment = Assignment(999, "Test Assignment", date.today())
        self.repo.add_assignments(assignment)
        retrieved_assignment = self.repo.get_by_id_assignments(999)
        self.assertEqual(retrieved_assignment, assignment)

    def test_add_existing_assignment(self):
        assignment = Assignment(2001, "Existing Assignment", date.today())
        with self.assertRaises(RepositoryException):
            self.repo.add_assignments(assignment)

    def test_remove_assignment(self):
        assignment_id = 2001
        self.repo.remove_assignments(assignment_id)
        self.assertIsNone(self.repo.get_by_id_assignments(assignment_id))

    def test_remove_nonexistent_assignment(self):
        nonexistent_assignment_id = 9999
        with self.assertRaises(RepositoryException):
            self.repo.remove_assignments(nonexistent_assignment_id)

    def test_update_assignment(self):
        assignment = Assignment(2002, "Original Description", date.today())
        self.repo.update_assignments(assignment)
        updated_assignment = self.repo.get_by_id_assignments(2002)
        self.assertEqual(updated_assignment.description, "Original Description")

    def test_update_nonexistent_assignment(self):
        nonexistent_assignment = Assignment(9999, "Nonexistent Assignment", date.today())
        with self.assertRaises(RepositoryException):
            self.repo.update_assignments(nonexistent_assignment)

    def test_str(self):
        self.assertEqual(str(Assignment(2006, "project", date(2023, 6, 3))), str(self.__assignments[2006]))
        self.assertEqual(self.repo.assignment(), self.repo.assignment())

    def test_assignment_services(self):
        assign = Assignment(2002, "Original Description", date.today())
        self.assign.add(2022, "project", date.today())
        self.assertEqual(len(self.repo.assignment()), 21)

        self.assign.update(2022, "Original Description", date.today())
        self.assertEqual(self.repo.get_by_id_assignments(2022), Assignment(2022, "Original Description", date.today()))

        self.assign.remove(2022)
        self.assertEqual(len(self.repo.assignment()), 20)
