from src.domain.student import Student
from src.repository.memory_repository import MemoryRepository


class StudentServices:
    def __init__(self, student_repo: MemoryRepository):
        self.repo = student_repo

    def add(self, _id: int, name: str, group: int):
        student = Student(_id, name, group)
        self.repo.add_students(student)

    def remove(self, _id: int):
        self.repo.remove_students(_id)

    def list(self):
        self.repo.list_students()

    def update(self, _id: int, name: str, group: int):
        student = Student(_id, name, group)
        self.repo.update_students(student)
