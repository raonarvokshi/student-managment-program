from colorama import Fore
import time
import os
import json


class Students:
    students = []

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def add_student(self):
        new_student = {
            "name": self.name,
            "age": self.age,
            "subject": self.subject
        }
        Students.students.append(new_student)
        print("Student was added successfully!\n")

    @classmethod
    def show_all_students(cls):
        if not cls.students:
            print(f"{Fore.LIGHTBLUE_EX}Loading students...")
            time.sleep(3)
            cls.clear_screen()

            print(f"{Fore.RED}No saved students found.\n")
        else:
            print(f"{Fore.LIGHTBLUE_EX}Loading students...")
            time.sleep(3)
            cls.clear_screen()
            for student in cls.students:
                print(f"{Fore.GREEN}{student}\n")

    @classmethod
    def filter_student_by_name(cls):
        filter_name = input("Enter student name: ")
        cls.clear_screen()

        print(f"{Fore.LIGHTBLUE_EX}Loading student...")
        time.sleep(3)
        cls.clear_screen()

        found_students = []
        for student in cls.students:
            if student["name"] == filter_name:
                found_students.append(student)

        if found_students:
            if len(found_students) == 1:
                print(
                    f"{Fore.CYAN}Found {len(found_students)} student with the name {filter_name}:\n")
            else:
                print(
                    f"{Fore.CYAN}Found {len(found_students)} students with the name {filter_name}:\n")

            for student in found_students:
                for key, value in student.items():
                    print(f"{Fore.GREEN}{key}: {value}")
                print("\n")
        else:
            print(f"{Fore.RED}No student found with the name {filter_name}.")

    @classmethod
    def filter_student_by_age(cls):
        from_age = int(input(f"{Fore.WHITE}Enter from age: "))
        to_age = int(input(f"{Fore.WHITE}Enter to age: "))
        cls.clear_screen()
        filtered_students = [
            student for student in cls.students if from_age <= student["age"] <= to_age]

        if not filtered_students:
            print(f"{Fore.LIGHTBLUE_EX}Loading student...\n")
            time.sleep(2)
            cls.clear_screen()
            print(
                f"{Fore.RED}No students found in the age range {from_age} to {to_age}.")
        else:
            print(f"{Fore.LIGHTBLUE_EX}Loading student...\n")
            time.sleep(3)
            cls.clear_screen()
            print(
                f"{Fore.CYAN}Students in the age range {from_age} to {to_age}:\n")
            for student in filtered_students:
                print(f"{Fore.GREEN}{student}\n")

    @classmethod
    def filter_student_by_subject(cls):
        stud_subj = input("Enter student subject: ")
        cls.clear_screen()

        filtered_students = [
            student for student in cls.students if student["subject"] == stud_subj]

        if not filtered_students:
            print(f"{Fore.LIGHTBLUE_EX}Loading students...")
            time.sleep(3)
            cls.clear_screen()

            print(f"{Fore.RED}No students found with the subject: {stud_subj}\n")
        else:
            print(f"{Fore.LIGHTBLUE_EX}Loading students...")
            time.sleep(3)
            cls.clear_screen()

            print(f"{Fore.CYAN}Students with the subject: {stud_subj}\n")
            for student in filtered_students:
                print(f"{Fore.GREEN}{student}\n")

    @classmethod
    def save_students_to_file(cls, filename="students.json"):
        with open(filename, 'w') as file:
            json.dump(cls.students, file)

    @classmethod
    def load_students_from_file(cls, filename="students.json"):
        try:
            with open(filename, 'r') as file:
                cls.students = json.load(file)
        except FileNotFoundError:
            print(f"{Fore.RED}No saved students found.\n")

    @staticmethod
    def clear_screen():
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
