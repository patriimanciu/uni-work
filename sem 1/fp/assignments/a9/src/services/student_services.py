from src.domain.student import Student
from src.repository.memory_repo import MemoryRepository
from src.services.grade_services import GradeServices
from src.services.undo_service import Command, Operation, UndoService


class StudentServices:
    def __init__(self, student_repo: MemoryRepository, undo_manager: UndoService, grade_service: GradeServices):
        self.repo = student_repo
        self.undo_manager = undo_manager
        self.grade_service = grade_service

    def add(self, _id: int, name: str, group: int):
        # add is instance for all functions
        student = Student(_id, name, group)
        command_undo = Command(self.repo.remove_students, [student.id])
        command_redo = Command(self.repo.add_students, [student])
        operation = Operation(command_undo, command_redo)
        self.undo_manager.record(operation)
        self.repo.add_students(student)

    def remove_student(self, student):
        grades_to_delete = self.repo.assignments_by_student_id(student.id).copy()
        graded_assignments = {}
        # print(grades_to_delete)

        for grade_key in grades_to_delete:
            # print(grade_key)
            # print(grade)
            print(self.repo.get_by_id_grades(grade_key))
            if self.repo.get_by_id_grades(grade_key).grade:
                graded_assignments[grade_key] = self.repo.get_by_id_grades(grade_key).grade
        # self.repo.remove_students(student.id)

        return grades_to_delete, graded_assignments

    """
    def remove(self, _id: int):
        student = self.repo.get_by_id_students(_id)
        grades_to_delete, graded_assignments = self.remove_student(student)
        # print(grades_to_delete)
        # print(graded_assignments)

        command_undo = Command(self.undo_remove_student, [student, grades_to_delete, graded_assignments])
        command_redo = Command(self.repo.remove_students, [_id])
        operation = Operation(command_undo, command_redo)
        self.repo.remove_students(_id)
        self.undo_manager.record(operation)
        # print(operation)
    """

    def undo_remove_student(self, student, grades_to_restore, graded_assignments):
        self.repo.add_students(student)

        for grade_key in grades_to_restore:
            self.repo.assign_to_student(grade_key[0], student.id)

        for grade_key in graded_assignments:
            # print(grade_key)
            # print(self.repo.get_by_id_grades(grade_key))
            # print(graded_assignments[grade_key])
            self.repo.grade_student(grade_key[0], grade_key[1], graded_assignments[grade_key])

    def remove(self, _id: int):
        student = self.repo.get_by_id_students(_id)
        grades_to_delete, graded_assignments = self.remove_student(student)
        command_undo = Command(self.undo_remove_student, [student, grades_to_delete, graded_assignments])
        command_redo = Command(self.repo.remove_students, [student.id])
        operation = Operation(command_undo, command_redo)
        self.undo_manager.record(operation)
        self.repo.remove_students(_id)

    def list(self):
        return self.repo.list_students()

    def update(self, _id: int, name: str, group: int):
        original_student = self.repo.get_by_id_students(_id)
        new_student = Student(_id, name, group)
        # print(str(original_student) + " " + str(new_student))
        command_undo = Command(self.repo.update_students, [Student(original_student.id, original_student.name, original_student.group)])
        command_redo = Command(self.repo.update_students, [new_student])
        operation = Operation(command_undo, command_redo)
        self.undo_manager.record(operation)
        self.repo.update_students(new_student)
