"""
3. Students
    Manage a list of students. Each student has an id (integer, unique), a name (string) and a group (positive integer).
    Provide the following features:

    Add a student. Student data is read from the console.
    Display the list of students.
    Filter the list so that students in a given group (read from the console) are deleted from the list.
    Undo the last operation that modified program data. This step can be repeated.
        The user can undo only those operations made during the current run of the program.
"""
from colorama import Fore, Style
from src.domain.domain import Student
from src.repository.repository import MemoryRepository, TextFileRepository, BinaryFileRepository
from random import randint, choice


def to_int(n: str):
    try:
        m = int(n)
        return True
    except ValueError:
        return False


class UI:
    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    def display_error(message):
        print(Fore.RED + f"Error: {message}" + Style.RESET_ALL)

    @staticmethod
    def parse_command(command):
        tokens = command.split()
        action = tokens[0].lower()
        args = tokens[1:]
        return action, args

    @staticmethod
    def get_user_input():
        print()
        print(Fore.LIGHTMAGENTA_EX + "--------------------------------------")
        commands = """
        add <student_id> <name> <group>
        list
        filter <group>
        undo     
        exit    
        """
        print()
        print("Supported commands look like this:")
        print(f"{commands}")
        print("--------------------------------------")
        print("" + Style.RESET_ALL)
        return input("Enter command: ")

    # command line application
    def run(self):
        while True:
            command = UI.get_user_input()
            if command:
                action, args = UI.parse_command(command)
            else:
                print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                continue

            if action == 'add':
                if len(args) == 3:
                    try:
                        if to_int(args[0]) and to_int(args[2]):
                            student_id = int(args[0])
                            name = args[1]
                            group = int(args[2])
                            student = Student(student_id, name, group)
                            self.repository.add_student(student)
                        else:
                            print(Fore.RED + "The input is invalid" + Style.RESET_ALL)
                    except ValueError as ve:
                        print(Fore.RED + "Something went wrong. " + str(ve) + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Not enough / too many arguments" + Style.RESET_ALL)

            elif action == 'list':
                self.repository.display_students()

            elif action == 'filter':
                if len(args) == 1:
                    if to_int(args[0]):
                        group_to_filter = int(args[0])
                        self.repository.filter_students(group_to_filter)
                    else:
                        print(Fore.RED + "Something went wrong. The input is not valid." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Too many arguments" + Style.RESET_ALL)

            elif action == 'undo':
                try:
                    self.repository.undo()
                except ValueError as ve:
                    print(Fore.RED + str(ve) + Style.RESET_ALL)

            elif action == 'exit':
                if isinstance(self.repository, TextFileRepository):
                    self.repository.save_to_file('students_data.txt')
                elif isinstance(self.repository, BinaryFileRepository):
                    self.repository.save_to_file('students.data')
                print(Fore.GREEN + "Bye! :) " + Style.RESET_ALL)
                break

            else:
                self.display_error("Command not supported.")


def generate_random_stud():
    initial_students = []
    names = ["Alex", "Ana", "Maria", "John", "Luke", "Matthew", "Iris", "Aris", "David", "Lorena", "Melisa", "Kate"]
    first_id = randint(11001, 12000)
    for i in range(10):
        name = choice(names)
        group = randint(910, 917)
        stud_id = first_id + i
        new_stud = Student(stud_id, name, group)
        initial_students.append(new_stud)

    return initial_students

