from src.domain.domain import Student


class Services:
    def __init__(self, repo):
        self.repo = repo

    def add_student(self, student: Student):
        """
        Calls the add_student function from the repo module
        :param student: new student to be added
        :return:
        """
        self.repo.add_student(student)

    # TODO separate service and repo tests

    def display_students(self):
        return self.repo.display_students()

    def filter_students(self, group):
        return self.repo.filter_students(group)
