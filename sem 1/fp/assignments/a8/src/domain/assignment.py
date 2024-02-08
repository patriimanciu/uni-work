from datetime import date
from random import choice, randint

from src.domain.idobject import IdObject


class Assignment(IdObject):
    def __init__(self, _id: int, description: str, deadline: date):
        super().__init__(_id)
        # if not isinstance(student, Student) and student is not None:
        #     raise TypeError("The student must be... a student :) ")
        # self.__students = [student]
        self.__description = description
        if not isinstance(deadline, date):
            raise TypeError("The deadline must be of type 'date'.")
        self.__deadline = deadline

    def __str__(self):
        return f"Assignment ID: {self.id}, Description: {self.description}, Deadline: {self.deadline}"

    def __eq__(self, other):
        if not isinstance(other, Assignment):
            return False
        return self.id == other.id

    # @property
    # def student(self):
    #     return self.__students

    @property
    def description(self):
        return self.__description

    @property
    def deadline(self):
        return self.__deadline

    # @student.setter
    # def student(self, new_stud):
    #     self.__student = new_stud

    @description.setter
    def description(self, desc):
        self.__description = desc

    @deadline.setter
    def deadline(self, dead):
        self.__deadline = dead


def generate_assignments(n: int) -> dict:
    """
    :param n: number of generated assignments
    :return:
    """
    assignments = {}
    _id = 2000
    desc = ["project", "coding assignment", "essay", "problem sheet", "research"]
    for i in range(n):
        random_date = date(2023, randint(1, 12), randint(1, 28))
        assignments[_id + 1] = Assignment(_id + 1, choice(desc), random_date)
        _id += 1
    return assignments
