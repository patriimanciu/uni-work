from src.repository.repository import MemoryRepository, TextFileRepository, BinaryFileRepository
from src.ui.UI import generate_random_stud, UI


def get_repo():
    with open("choose.properties", "r") as settings_file:
        for line in settings_file:
            line = line.strip()
            if line.startswith("REPOSITORY="):
                repository_type = line[len("REPOSITORY="):]
                if repository_type == "memory":
                    return MemoryRepository()
                elif repository_type == "text":
                    return TextFileRepository("students_data.txt")
                elif repository_type == "binary":
                    return BinaryFileRepository("students.data")
                else:
                    raise ValueError("Invalid repository type!")
            else:
                raise ValueError("Invalid settings file!")


if __name__ == "__main__":
    initial_stud = generate_random_stud()
    repository = get_repo()
    if isinstance(repository, TextFileRepository):
        repository.load_from_file('students_data.txt')
    elif isinstance(repository, BinaryFileRepository):
        repository.load_from_file('students.data')

    if not repository.students:
        for stud in initial_stud:
            repository.add_student_initial(stud)
    else:
        repository.changes = []

    ui = UI(repository)
    ui.run()
