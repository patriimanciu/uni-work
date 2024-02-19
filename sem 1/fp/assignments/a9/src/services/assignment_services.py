from datetime import date

from src.domain.assignment import Assignment
from src.repository.memory_repo import MemoryRepository, RepositoryException
from src.services.grade_services import GradeServices
from src.services.undo_service import UndoService, Command, Operation


class AssignmentServices:
    def __init__(self, assignment_repo: MemoryRepository, undo_manager: UndoService, grade_service: GradeServices):
        self.repo = assignment_repo
        self.undo_manager = undo_manager
        self.grade_service = grade_service

    def add(self, _id: int, description: str, deadline: date):
        if deadline.year < 2022:
            raise RepositoryException("Date is invalid.")
        assign = Assignment(_id, description, deadline)
        command_undo = Command(self.repo.remove_assignments, [assign.id])
        command_redo = Command(self.repo.add_assignments, [assign])
        operation = Operation(command_undo, command_redo)
        self.undo_manager.record(operation)
        self.repo.add_assignments(assign)

    def remove_assignment(self, assignment):
        grades_to_delete = self.repo.grades_by_assignment_id(assignment.id)
        graded_assignments = {}
        print(grades_to_delete)

        for grade_key in grades_to_delete:
            print(grade_key)
            print(self.repo.get_by_id_grades(grade_key))
            if self.repo.get_by_id_grades(grade_key).grade:
                graded_assignments[grade_key] = self.repo.get_by_id_grades(grade_key).grade
        self.repo.remove_assignments(assignment.id)
        return grades_to_delete, graded_assignments

    def remove(self, _id: int):
        assignment = self.repo.get_by_id_assignments(_id)
        grades_to_delete, graded_assignments = self.remove_assignment(assignment)
        command_undo = Command(self.undo_remove_assignments, [assignment, grades_to_delete, graded_assignments])
        command_redo = Command(self.repo.remove_assignments, [assignment.id])
        operation = Operation(command_undo, command_redo)
        self.undo_manager.record(operation)

    def undo_remove_assignments(self, assignment, grades_to_restore, graded_assignments):
        self.repo.add_assignments(assignment)
        for grade_key in grades_to_restore:
            print(grade_key)
            self.grade_service.assign_to_student(grade_key[0], [grade_key[1]])
        for grade_key in graded_assignments:
            print(grade_key)
            print(self.repo.get_by_id_grades(grade_key))
            print(graded_assignments[grade_key])
            self.grade_service.grade_student(grade_key[0], grade_key[1], graded_assignments[grade_key])

    def list(self):
        return self.repo.list_assignments()

    def update(self, _id: int, description: str, deadline: date):
        original_assignment = self.repo.get_by_id_assignments(_id)
        new_assignment = Assignment(_id, description, deadline)
        command_undo = Command(self.repo.update_assignments, [Assignment(original_assignment._id, original_assignment.description, original_assignment.deadline)])
        command_redo = Command(self.repo.update_assignments, [new_assignment])
        operation = Operation(command_undo, command_redo)
        self.undo_manager.record(operation)
        self.repo.update_assignments(new_assignment)
