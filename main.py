import json
import os
import time
from colorama import Fore
from students import Students

program_on = True


Students.load_students_from_file()


def start_program():
    global program_on
    while program_on:
        try:
            print(f"{Fore.RESET}1. Add Student")
            print(f"{Fore.RESET}2. Show Students")
            print(f"{Fore.RESET}3. Search Student By Name")
            print(f"{Fore.RESET}4. Search Student By Age")
            print(f"{Fore.RESET}5. Search Student By Subject")
            options = int(input("Choose one of the options: "))
            Students.clear_screen()

            if options == 1:
                student_name = input("Enter student name: ")
                student_age = int(input("Enter student age: "))
                student_subject = input("Enter student subject: ")
                student = Students(name=student_name, age=student_age,
                                   subject=student_subject)
                student.add_student()
            elif options == 2:
                Students.show_all_students()

            elif options == 3:
                Students.filter_student_by_name()

            elif options == 4:
                Students.filter_student_by_age()

            elif options == 5:
                Students.filter_student_by_subject()

            else:
                print(f"{Fore.RED}Invalid option.")

        except ValueError:
            Students.clear_screen()
            print(f"{Fore.RED}Enter an option from 1 to 4!")
            time.sleep(3)

        print(
            f"{Fore.RESET}Do you want to continue using the program or quit the program")
        continue_program = input(
            f"{Fore.RESET}Enter 'continue' or 'quit': ").lower()
        Students.clear_screen()

        if continue_program != "continue":
            program_on = False
            # Save students to file when the program ends
            Students.save_students_to_file()
            print(f"{Fore.GREEN}Program quit successfully")
            break


start_program()
