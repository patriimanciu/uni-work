from src.repository.memory_repo import MemoryRepository, RepositoryException
from src.services.undo_service import UndoService, Command, Operation


class GradeServices:
    def __init__(self, grade_repo: MemoryRepository, undo_manager: UndoService):
        self.repo = grade_repo
        self.undo_manager = undo_manager

    def assign_to_student(self, assignment_id: int, student_ids: list):
        assignment = self.repo.get_by_id_assignments(assignment_id)
        if not assignment:
            raise RepositoryException("Assignment not found.")

        for student_id in student_ids:
            stud = self.repo.get_by_id_students(int(student_id))
            if not stud:
                raise RepositoryException("No student found.")
            undo_operation = Command(self.repo.unassign_from_student, [int(assignment_id), int(student_id)])
            redo_operation = Command(self.repo.assign_to_student, [int(assignment_id), int(student_id)])
            self.undo_manager.record(Operation(undo_operation, redo_operation))
            self.repo.assign_to_student(assignment_id, int(student_id))

    def assignments_by_student_id(self, student_id: int):
        self.repo.assignments_by_student_id(student_id)

    def unassign_from_student(self, assignment_id: int, student_id: int):
        self.repo.unassign_from_student(assignment_id, student_id)

    def grade_student(self, assignment_id, student_id, grade_value):
        undo_operation = Command(self.repo.set_grade_none, [int(assignment_id), int(student_id)])
        redo_operation = Command(self.repo.grade_student, [int(assignment_id), int(student_id), int(grade_value)])
        operation = Operation(undo_operation, redo_operation)
        self.undo_manager.record(operation)
        self.repo.grade_student(assignment_id, student_id, grade_value)

    def list(self):
        return self.repo.list_grades()
