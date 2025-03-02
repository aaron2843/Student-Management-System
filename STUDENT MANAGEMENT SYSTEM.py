class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.courses = []
        self.grades = {}
        self.attendance = {}

    def register_course(self, course_name):
        self.courses.append(course_name)
        self.grades[course_name] = None
        self.attendance[course_name] = 0

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.grades[course_name] = grade
        else:
            print("You are not registered for this course.")

    def mark_attendance(self, course_name):
        if course_name in self.courses:
            self.attendance[course_name] += 1
        else:
            print("You are not registered for this course.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print("Courses Registered:")
        for course in self.courses:
            print(f"- {course}")
        print("Grades:")
        for course, grade in self.grades.items():
            print(f"- {course}: {grade}")
        print("Attendance:")
        for course, attend in self.attendance.items():
            print(f"- {course}: {attend} times")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, email, password):
        if email in self.students:
            print("Student with this email already exists.")
        else:
            self.students[email] = Student(name, email, password)
            print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("Student List:")
            for student in self.students.values():
                print(student)

    def update_student(self, email, name=None, password=None):
        if email in self.students:
            if name:
                self.students[email].name = name
            if password:
                self.students[email].password = password
            print(f"Student with email {email} updated successfully!")
        else:
            print("Student not found.")

    def delete_student(self, email):
        if email in self.students:
            del self.students[email]
            print(f"Student with email {email} deleted successfully!")
        else:
            print("Student not found.")

    def login_student(self, email, password):
        if email in self.students and self.students[email].password == password:
            return self.students[email]
        else:
            return None

def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Login as Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            sms.add_student(name, email, password)
        elif choice == "2":
            sms.view_students()
        elif choice == "3":
            email = input("Enter student email to update: ")
            name = input("Enter new name (leave blank to keep unchanged): ")
            password = input("Enter new password (leave blank to keep unchanged): ")
            sms.update_student(email, name if name else None, password if password else None)
        elif choice == "4":
            email = input("Enter student email to delete: ")
            sms.delete_student(email)
        elif choice == "5":
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            student = sms.login_student(email, password)
            if student:
                print("Login successful!")
                while True:
                    print("\nStudent Menu")
                    print("1. Register Course")
                    print("2. Update Grade")
                    print("3. Mark Attendance")
                    print("4. Display Info")
                    print("5. Logout")

                    student_choice = input("Enter your choice: ")

                    if student_choice == "1":
                        course_name = input("Enter course name: ")
                        student.register_course(course_name)
                        print(f"Course '{course_name}' registered successfully!")
                    elif student_choice == "2":
                        course_name = input("Enter course name: ")
                        grade = input("Enter grade: ")
                        student.update_grade(course_name, grade)
                        print(f"Grade for course '{course_name}' updated to {grade}.")
                    elif student_choice == "3":
                        course_name = input("Enter course name: ")
                        student.mark_attendance(course_name)
                        print(f"Attendance for course '{course_name}' marked.")
                    elif student_choice == "4":
                        student.display_info()
                    elif student_choice == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid email or password.")
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
