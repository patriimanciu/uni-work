"""
2. Student Lab Assignment
Write an application that manages student lab assignments for a discipline. The application will store:

Student: student_id, name, group
Assignment: assignment_id, description, deadline
Grade: assignment_id, student_id, grade_value
Create an application that allows to:

Manage students and assignments. The user can add, remove, update, and list both students and assignments.
Give assignments to a student or a group of students. In case an assignment is given to a group of students, every student in the group will receive it. In case there are students who were previously given that assignment, it will not be assigned again.
Grade student for a given assignment. When grading, the program must allow the user to select the assignment that is graded, from the student’s list of ungraded assignments. A student’s grade for a given assignment cannot be changed. Deleting a student removes their assignments. Deleting an assignment also removes all grades at that assignment.
Create statistics:
All students who received a given assignment, ordered descending by grade.
All students who are late in handing in at least one assignment. These are all the students who have an ungraded assignment for which the deadline has passed.
Students with the best school situation, sorted in descending order of the average grade received for all graded assignments.
"""
from datetime import date

from colorama import Fore, Style

from src.repository.binary_file_repo import BinaryFileRepository
from src.repository.memory_repo import MemoryRepository
from src.repository.text_file_repo import TextFileRepository
from src.services.assignment_services import AssignmentServices
from src.services.grade_services import GradeServices
from src.services.student_services import StudentServices
from src.services.undo_service import UndoService
from src.ui.setup import Setup


class UI(Setup):
    def __init__(self):
        super().__init__()
        self.undo_redo = UndoService()
        self.grades = GradeServices(self.repository, self.undo_redo)
        self.stud = StudentServices(self.repository, self.undo_redo, self.grades)
        self.assign = AssignmentServices(self.repository, self.undo_redo, self.grades)

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
        undo
        redo
        exit
        """
        print()
        print("Supported commands look like this:")
        print(f"{commands}")
        print("--------------------------------------")
        print("" + Style.RESET_ALL)
        return input("Enter command: ")

    # ADD
    def add_student(self):
        try:
            _id = int(input("ID: "))
            name = input("Name: ")
            group = int(input("Group: "))
            self.stud.add(_id, name, group)
        except Exception as err:
            print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

    def add_assignment(self):
        try:
            _id = int(input("ID: "))
            description = input("Description: ")
            year = int(input("Deadline, Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))
            self.assign.add(_id, description, date(year, month, day))
        except Exception as err:
            print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

    # REMOVE
    def remove_student(self):
        try:
            _id = int(input("ID: "))
            self.stud.remove(_id)
        except Exception as err:
            print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

    def remove_assignment(self):
        try:
            _id = int(input("ID: "))
            self.assign.remove(_id)
        except Exception as err:
            print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

    # UPDATE
    def update_student(self):
        try:
            _id = int(input("ID: "))
            name = input("Name: ")
            group = int(input("Group: "))
            self.stud.update(_id, name, group)
        except Exception as err:
            print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

    def update_assignment(self):
        try:
            _id = int(input("ID: "))
            description = input("Description: ")
            year = int(input("Deadline, Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))
            self.assign.update(_id, description, date(year, month, day))
        except Exception as err:
            print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

    # Give & Grade assignments
    def give_assignment(self):
        try:
            assign_id = int(input("Assignment ID: "))
            student_ids = input("Student ID (if you want to assign it to multiple students, please separate "
                                "them by a ' '): ")
            tokens = student_ids.split()
            self.grades.assign_to_student(assign_id, tokens)
        except Exception as err:
            print(Fore.RED + "Not valid inputs: " + str(err) + Style.RESET_ALL)

    # Listing data
    def list_students(self):
        students = self.stud.list()
        print("List of Students:")
        for student in students:
            print(str(student))

    def list_assignments(self):
        assignments = self.assign.list()
        print("List of Assignments:")
        for assign in assignments:
            print(str(assign))

    def list_grades(self):
        grade = self.grades.list()
        print("List of Grades:")
        for grd in grade:
            print(str(grd))

    def run(self):
        self.get_settings()
        """if not self.repository.students():
            self.repository.students_setter(self.set_initial_students())
        if not self.repository.assignment():
            self.repository.assignments_setter(self.set_initial_assignments())
        if not self.repository.grades():
            self.repository.grades_setter(self.set_initial_grades())"""
        self.list_students()
        print()
        print("--------------------------------------")
        print()
        self.list_assignments()
        print()
        print("--------------------------------------")
        print()
        self.list_grades()
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
                # self.undo_redo.reset_history()
                if arg == "student":
                    self.add_student()
                elif arg == "assignment":
                    self.add_assignment()
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "remove":
                # self.undo_redo.reset_history()
                if arg == "student":
                    self.remove_student()
                elif arg == "assignment":
                    self.remove_assignment()
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "update":
                # self.undo_redo.reset_history()
                if arg == "student":
                    self.update_student()
                elif arg == "assignment":
                    self.update_assignment()
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "list":
                if arg == "student":
                    self.list_students()
                elif arg == "assignment":
                    self.list_assignments()
                elif arg == "grades":
                    self.list_grades()
                else:
                    print(Fore.RED + "Not a valid command" + Style.RESET_ALL)
                    continue

            elif action == "assign":
                # self.undo_redo.reset_history()
                self.give_assignment()

            elif action == "grade":
                """
                    When grading, the program must allow the user to select the assignment that is graded, 
                    from the student’s list of ungraded assignments.
                """
                self.undo_redo.reset_history()
                try:
                    student_id = int(input("Student ID: "))
                    student_assignments = self.repository.assignments_by_student_id(student_id)
                    if not student_assignments:
                        print(f"No assignments found for student with ID {student_id}")
                        continue
                except Exception as err:
                    print(Fore.RED + "An error occurred: " + str(err) + Style.RESET_ALL)

                print("Assignments for the student:")
                for (assignment_id, student_id), assignment_instance in student_assignments.items():
                    assign = self.repository.get_by_id_assignments(assignment_id)
                    print(
                        f"Assignment ID: {assignment_id}, Description: {assign.description}, Deadline: {assign.deadline}")

                try:
                    assignment_id = int(input("Enter Assignment ID to add a grade: "))
                    grade_value = int(input("Enter Grade Value: "))
                except Exception as err:
                    print(Fore.RED + "An error occurred: " + str(err) + Style.RESET_ALL)
                try:
                    self.grades.grade_student(assignment_id, student_id, grade_value)
                    print(Fore.GREEN + "Grade added successfully" + Style.RESET_ALL)
                except Exception as err:
                    print(Fore.RED + "An error occurred: " + str(err) + Style.RESET_ALL)

            elif action == "statistics":
                print(Fore.LIGHTMAGENTA_EX +
                        f" \n"
                        f"1. All students who received a given assignment, ordered descending by grade. \n"
                        f"2. All students who are late in handing in at least one assignment. \n"
                        f"   These are all the students who have an ungraded assignment for which the deadline has passed.\n"
                        f"3. Students with the best school situation, sorted in descending order of the average grade \n"
                        f"   received for all graded assignments.\n" + Style.RESET_ALL)

                option = input("> ")
                if option == "1":
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
                    for stud_id, grade in best_stud:
                        print(str(self.repository.get_by_id_students(stud_id)) + " -> " + str(grade))

            elif action == "undo":
                # print(self.undo_redo.list_history())
                try:
                    self.undo_redo.undo()
                except Exception as err:
                    print(Fore.RED + "An error occurred: " + str(err) + Style.RESET_ALL)

            elif action == "redo":
                try:
                    self.undo_redo.redo()
                except Exception as err:
                    (Fore.RED + "An error occurred: " + str(err) + Style.RESET_ALL)

            elif action == "exit":
                print(Fore.GREEN + "Bye! :) " + Style.RESET_ALL)
                if isinstance(self.repository, TextFileRepository):
                    self.repository.save_data_text()
                elif isinstance(self.repository, BinaryFileRepository):
                    self.repository.save_data_binary()
                break

            else:
                print(Fore.RED + "Command not supported." + Style.RESET_ALL)
