class Student:
    def __init__(self, student_id: int, student_name: str, group: int):
        self.__id = student_id
        self.__name = student_name
        self.__group = group

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def group(self):
        return self.__group

    def __eq__(self, other):
        return self.__id == other.__id
