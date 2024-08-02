# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: Data processing using dictionaries and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Aisling,7/31/2024,Updated Script to meet acceptance criteria
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
json_data: str = ''
file = None
menu_choice: str = ''

# When the program starts, the contents of json are read into a two-dimensional list table
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"{FILE_NAME} not found. Starting with an empty list.")
except json.JSONDecodeError:
    print(f"Error reading {FILE_NAME}. Starting with an empty list.")
except Exception as e:
    print(f"An error occurred: {e}")

# Process and read back to user the data
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        # Register a student for a course
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
        except ValueError as e:
            print(e)
            continue

        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
        except ValueError as e:
            print(e)
            continue

        course_name = input("Please enter the name of the course: ")
        student_data = {"first_name": student_first_name, "last_name": student_last_name, "course": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    elif menu_choice == "2":
        # Show current data
        print("-" * 50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course']}")
        print("-" * 50)
        continue

    elif menu_choice == "3":
        # Save the data to a file
        try:
            with open(FILE_NAME, "w") as file:
                # Write content into file
                json.dump(students, file)
            print("Your data was saved")
            for student in students:
                print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course']}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
        continue

    elif menu_choice == "4":
        # Ends code
        break
    else:
        print("Please choose a viable option")

print("Program Ended")
