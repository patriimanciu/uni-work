from src.domain.domain import Student
from src.services.services import Services


class TestStud:
    """
    This class tests the functions from the service module.
    """
    def __init__(self, repository) -> None:
        self.students_service = Services(repository)

    def test_add(self):
        """
        Tests the add method from the service module.
        :return:
        """
        stud_data = self.students_service.repo
        count = len(stud_data)

        self.students_service.add_student(Student(101, "NEW", 914))
        assert len(self.students_service.display_students()) == count + 1

        self.students_service.add_student(Student(102, "Stud", 911))
        assert len(self.students_service.display_students()) == count + 2

        try:
            self.students_service.add_student(Student(102, "Stud", 911))
        except Exception:
            assert True
        assert len(self.students_service.display_students()) == count + 2
