from src.repository.memory_repository import MemoryRepository, RepositoryException


class GradeServices:
    def __init__(self, grade_repo: MemoryRepository):
        self.repo = grade_repo

    def assign_to_student(self, assignment_id: int, student_ids: list):
        assignment = self.repo.get_by_id_assignments(assignment_id)
        if not assignment:
            raise RepositoryException("Assignment not found.")

        for student_id in student_ids:
            stud = self.repo.get_by_id_students(int(student_id))
            if not stud:
                raise RepositoryException("No student found.")
            self.repo.assign_to_student(assignment_id, int(student_id))

    def assignments_by_student_id(self, student_id: int):
        self.repo.assignments_by_student_id(student_id)

    def grade_student(self, assignment_id, student_id, grade_value):
        self.repo.grade_student(assignment_id, student_id, grade_value)

    def list(self):
        self.repo.list_grades()
