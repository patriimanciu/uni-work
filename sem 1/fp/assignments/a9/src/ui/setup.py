from src.repository.binary_file_repo import BinaryFileRepository
from src.repository.memory_repo import MemoryRepository
from src.repository.text_file_repo import TextFileRepository
from src.domain.assignment import generate_assignments


class Setup:
    def __init__(self):
        self.repository = self.get_settings()
        # self.set_initial_students = generate_students(20)
        # self.set_initial_assignments = generate_assignments(20)
        # self.set_initial_grades = self.randomly_assign_assignments(25)

    @staticmethod
    def get_settings():
        repository_type = None
        file_paths = {}
        with open("settings.properties", "r") as settings_file:
            for line in settings_file:
                line = line.strip()
                if line.startswith("REPOSITORY="):
                    repository_type = line[len("REPOSITORY="):]
                elif line.startswith("STUDENTS="):
                    file_paths["students"] = line[len("STUDENTS="):]
                elif line.startswith("ASSIGNMENTS="):
                    file_paths["assignments"] = line[len("ASSIGNMENTS="):]
                elif line.startswith("GRADES="):
                    file_paths["grades"] = line[len("GRADES="):]
        if repository_type is not None:
            if repository_type == "memory":
                return MemoryRepository()
            elif repository_type == "text":
                return TextFileRepository(file_paths)
            elif repository_type == "binary":
                return BinaryFileRepository(file_paths)
        else:
            raise ValueError("Invalid settings file!")
