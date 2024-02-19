from src.domain.idobject import IdObject
from random import randint, choice


class Student(IdObject):
    def __init__(self, _id: int, name: str, group: int):
        super().__init__(_id)
        if not isinstance(name, str):
            raise TypeError("Name must be of type str.")
        self._name = name
        if not isinstance(group, int):
            raise TypeError("Group must be of type int.")
        self._group = group
    """
    def __str__(self):
        return f"{self.id} -> {self.__name}, {self.__group}"
        """

    def __eq__(self, other):
        if isinstance(other, Student):
            return (
                self.id == other.id and
                self.name == other.name and
                self.group == other.group
            )
        return False

    def __str__(self):
        return f"ID: {self.id} | Name: {self._name}, Group: {self._group}"

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @group.setter
    def group(self, new_group):
        self._group = new_group


def generate_students(n: int) -> dict:
    students_list = {}
    _id = 1000
    names = ["Samuel", "David", "Alex", "Andrei", "Maria", "Andreea", "Ioana",
             "Diana", "Meghan", "John", "Hosea", "Saul", "Paul", "Mara", "Matthew",
             "Kate", "Will", "Lucas", "Marcus"]

    for i in range(n):
        students_list[_id + 1] = Student(_id + 1, choice(names), randint(911, 917))
        _id = _id + 1
    return students_list
