from datetime import date

from src.domain.assignment import Assignment
from src.repository.memory_repository import MemoryRepository


class AssignmentServices:
    def __init__(self, assignment_repo: MemoryRepository):
        self.repo = assignment_repo

    def add(self, _id: int, description: str, deadline: date):
        assign = Assignment(_id, description, deadline)
        self.repo.add_assignments(assign)

    def remove(self, _id: int):
        self.repo.remove_assignments(_id)

    def list(self):
        self.repo.list_assignments()

    def update(self, _id: int, description: str, deadline: date):
        assign = Assignment(_id, description, deadline)
        self.repo.update_assignments(assign)