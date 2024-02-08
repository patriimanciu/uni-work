from datetime import date

from colorama import Fore, Style

from src.repository.memory_repository import MemoryRepository
from src.services.assignment_services import AssignmentServices
from src.services.grade_services import GradeServices
from src.services.student_services import StudentServices


class UI:
    def __init__(self):
        self.repository = MemoryRepository()
        self.stud = StudentServices(self.repository)
        self.assign = AssignmentServices(self.repository)
        self.grades = GradeServices(self.repository)
    """
    @staticmethod
    def parse_command(command):
        tokens = command.split()
        action = tokens[0].lower()
        arg = tokens[1].lower()
        return action, arg
    """

    @staticmethod
    def get_user_input():
        print()
        print(Fore.LIGHTMAGENTA_EX + "--------------------------------------")
        commands = """
        add student / assignment
        remove student / assignment
        update student / assignment
        list student / assignment / grades
        assign
        grade
        statistics
        exit
        """
        print()
        print("Supported commands look like this:")
        print(f"{commands}")
        print("--------------------------------------")
        print("" + Style.RESET_ALL)
        return input("Enter command: ")

    def run(self):
        print("Current students: ")
        self.stud.list()
        print()
        print("--------------------------------------")
        print()
        print("Current assignments: ")
        self.assign.list()
        while True:
            command = UI.get_user_input()
            args = command.split()

            if command:
                if len(args) == 1:
                    action = args[0].lower()
                elif len(args) == 2:
                    action = args[0].lower()
                    arg = args[1].lower()
                else:
                    print(Fore.RED + "The command must consist of at most 2 arguments." + Style.RESET_ALL)
                    continue
            else:
                print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                continue

            if action == "add":
                if arg == "student":
                    try:
                        _id = int(input("ID: "))
                        name = input("Name: ")
                        group = int(input("Group: "))
                        self.stud.add(_id, name, group)
                    except Exception as err:
                        print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)
                elif arg == "assignment":
                    try:
                        _id = int(input("ID: "))
                        description = input("Description: ")
                        year = int(input("Deadline, Year: "))
                        month = int(input("Month: "))
                        day = int(input("Day: "))
                        self.assign.add(_id, description, date(year, month, day))
                    except Exception as err:
                        print(Fore.RED + "Not valid inputs: " + str(err)  + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "remove":
                if arg == "student":
                    try:
                        _id = int(input("ID: "))
                        self.stud.remove(_id)
                    except Exception as err:
                        print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)
                elif arg == "assignment":
                    try:
                        _id = int(input("ID: "))
                        self.assign.remove(_id)
                    except Exception as err:
                        print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "update":
                if arg == "student":
                    try:
                        _id = int(input("ID: "))
                        name = input("Name: ")
                        group = int(input("Group: "))
                        self.stud.update(_id, name, group)
                    except Exception as err:
                        print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)
                elif arg == "assignment":
                    try:
                        _id = int(input("ID: "))
                        description = input("Description: ")
                        year = int(input("Deadline, Year: "))
                        month = int(input("Month: "))
                        day = int(input("Day: "))
                        self.assign.update(_id, description, date(year, month, day))
                    except Exception as err:
                        print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "list":
                if arg == "student":
                    self.stud.list()
                elif arg == "assignment":
                    self.assign.list()
                elif arg == "grades":
                    self.grades.list()
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "assign":
                try:
                    assign_id = int(input("Assignment ID: "))
                    student_ids = input("Student ID (if you want to assign it to multiple students, please separate "
                                        "them by a ' '): ")
                    tokens = student_ids.split()
                    self.grades.assign_to_student(assign_id, tokens)
                except Exception as err:
                    print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

            elif action == "grade":
                """
                    When grading, the program must allow the user to select the assignment that is graded, 
                    from the student’s list of ungraded assignments.
                """
                student_id = int(input("Student ID: "))
                student_assignments = self.repository.assignments_by_student_id(student_id)
                # print(student_assignments)
                if not student_assignments:
                    print(f"No assignments found for student with ID {student_id}")
                    continue

                print("Assignments for the student:")
                for (assignment_id, student_id), assignment_instance in student_assignments.items():
                    assign = self.repository.get_by_id_assignments(assignment_id)
                    print(
                        f"Assignment ID: {assignment_id}, Description: {assign.description}, Deadline: {assign.deadline}")

                assignment_id = int(input("Enter Assignment ID to add a grade: "))
                grade_value = int(input("Enter Grade Value: "))
                try:
                    self.grades.grade_student(assignment_id, student_id, grade_value)
                    print(Fore.GREEN + "Grade added successfully" + Style.RESET_ALL)
                except Exception as err:
                    print(Fore.RED + "An error occurred: " + str(err) + Style.RESET_ALL)

            elif action == "statistics":
                print(Fore.LIGHTMAGENTA_EX + f" \n"
                      f"1. All students who received a given assignment, ordered descending by grade. \n"
                      f"2. All students who are late in handing in at least one assignment. \n"
                      f"   These are all the students who have an ungraded assignment for which the deadline has passed. \n"
                      f"3. Students with the best school situation, sorted in descending order of the average grade \n"
                      f"   received for all graded assignments.\n" + Style.RESET_ALL)

                option = input("> ")
                if option == "1":
                    # TODO figure out how to print out nicely
                    assignment_id = int(input("Assignment ID: "))
                    students_desc = self.repository.students_received_assignment(assignment_id)
                    for stud, grade in students_desc:
                        print(str(self.repository.get_by_id_students(stud)) + " -> " + str(grade))
                elif option == "2":
                    late_stud = self.repository.late_students()
                    for stud in late_stud:
                        print(str(self.repository.get_by_id_students(stud)))
                elif option == "3":
                    best_stud = self.repository.best_performance_students()
                    # print(best_stud)
                    for stud_id, grade in best_stud:
                       print(str(self.repository.get_by_id_students(stud_id)) + " -> " + str(grade))


            elif action == "exit":
                    print(Fore.GREEN + "Bye! :) " + Style.RESET_ALL)
                    break

            else:
                    print(Fore.RED + "Command not supported." + Style.RESET_ALL)
