import pandas as pd
from datetime import datetime, timedelta

# Create a DataFrame to store student grades
columns = ['Student_ID', 'Student_Name', 'Subject', 'Grade', 'Date']
grades_df = pd.DataFrame(columns=columns)

# Function to add a student's grade
def add_grade(student_id, student_name, subject, grade):
    global grades_df
    current_date = datetime.now()
    new_entry = pd.DataFrame({
        'Student_ID': [student_id],
        'Student_Name': [student_name],
        'Subject': [subject],
        'Grade': [grade],
        'Date': [current_date]
    })
    grades_df = pd.concat([grades_df, new_entry], ignore_index=True)
    print("\nGrade added successfully!")

# Function to update a student's grade
def update_grade(student_id, subject, new_grade):
    global grades_df
    mask = (grades_df['Student_ID'] == student_id) & (grades_df['Subject'] == subject)
    
    if not grades_df[mask].empty:
        grades_df.loc[mask, 'Grade'] = new_grade
        grades_df.loc[mask, 'Date'] = datetime.now()
        print("\nGrade updated successfully!")
    else:
        print("\nRecord not found!")

# Function to delete a student's grade by ID and subject
def delete_grade(student_id, subject):
    global grades_df
    mask = (grades_df['Student_ID'] == student_id) & (grades_df['Subject'] == subject)
    
    if not grades_df[mask].empty:
        grades_df = grades_df.drop(grades_df[mask].index)
        print("\nGrade deleted successfully!")
    else:
        print("\nRecord not found!")

# Function to delete a specific student record by ID, name, and subject
def delete_student(student_id, student_name, subject):
    global grades_df
    mask = (grades_df['Student_ID'] == student_id) & (grades_df['Student_Name'] == student_name) & (grades_df['Subject'] == subject)
    
    if not grades_df[mask].empty:
        grades_df = grades_df.drop(grades_df[mask].index)
        print("\nStudent record deleted successfully!")
    else:
        print("\nRecord not found!")

# Function to delete all grades
def delete_all_grades():
    global grades_df
    grades_df = pd.DataFrame(columns=['Student_ID', 'Student_Name', 'Subject', 'Grade', 'Date'])
    print("\nAll grades deleted successfully!")

# Function to view all grades
def view_grades():
    global grades_df
    print("\n--- All Grades ---")
    if grades_df.empty:
        print("No records found.")
    else:
        print(grades_df)

# Function to filter grades for the past one year
def view_grades_past_year():
    global grades_df
    one_year_ago = datetime.now() - timedelta(days=365)
    recent_grades = grades_df[grades_df['Date'] >= one_year_ago]
    print("\n--- Grades from the past year ---")
    if recent_grades.empty:
        print("No records found.")
    else:
        print(recent_grades)

# Function to save grades to a CSV file
def save_to_csv(filename='student_grades.csv'):
    global grades_df
    grades_df.to_csv(filename, index=False)
    print(f"\nGrades saved to {filename}")

# Function to load grades from a CSV file
def load_from_csv(filename='student_grades.csv'):
    global grades_df
    try:
        grades_df = pd.read_csv(filename)
        grades_df['Date'] = pd.to_datetime(grades_df['Date'])
        print(f"\nGrades loaded from {filename}")
    except FileNotFoundError:
        print(f"\nFile {filename} not found!")

# Function to save grades to an Excel file
def save_to_excel(filename='student_grades.xlsx'):
    global grades_df
    grades_df.to_excel(filename, index=False)
    print(f"\nGrades saved to {filename}")

# Function to load grades from an Excel file
def load_from_excel(filename='student_grades.xlsx'):
    global grades_df
    try:
        grades_df = pd.read_excel(filename)
        grades_df['Date'] = pd.to_datetime(grades_df['Date'])
        print(f"\nGrades loaded from {filename}")
    except FileNotFoundError:
        print(f"\nFile {filename} not found!")

# Menu-driven system
def menu():
    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Grade")
        print("2. Update Grade")
        print("3. Delete Grade by ID and Subject")
        print("4. Delete Student Record by ID, Name, and Subject")
        print("5. View All Grades")
        print("6. View Grades from Past Year")
        print("7. Save Grades to CSV")
        print("8. Load Grades from CSV")
        print("9. Save Grades to Excel")
        print("10. Load Grades from Excel")
        print("11. Delete All Grades")
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            subject = input("Enter Subject: ")
            grade = input("Enter Grade: ")
            add_grade(student_id, student_name, subject, grade)
        elif choice == 2:
            student_id = input("Enter Student ID: ")
            subject = input("Enter Subject: ")
            new_grade = input("Enter New Grade: ")
            update_grade(student_id, subject, new_grade)
        elif choice == 3:
            student_id = input("Enter Student ID: ")
            subject = input("Enter Subject: ")
            delete_grade(student_id, subject)
        elif choice == 4:
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            subject = input("Enter Subject: ")
            delete_student(student_id, student_name, subject)
        elif choice == 5:
            view_grades()
        elif choice == 6:
            view_grades_past_year()
        elif choice == 7:
            filename = input("Enter the CSV file name to save (e.g., 'grades.csv'): ")
            save_to_csv(filename)
        elif choice == 8:
            filename = input("Enter the CSV file name to load (e.g., 'grades.csv'): ")
            load_from_csv(filename)
        elif choice == 9:
            filename = input("Enter the Excel file name to save (e.g., 'grades.xlsx'): ")
            save_to_excel(filename)
        elif choice == 10:
            filename = input("Enter the Excel file name to load (e.g., 'grades.xlsx'): ")
            load_from_excel(filename)
        elif choice == 11:
            delete_all_grades()
        elif choice == 12:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the menu
menu()
