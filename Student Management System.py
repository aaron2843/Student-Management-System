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

    def register_student(self, name, email, password):
        self.students[email] = Student(name, email, password)

    def login_student(self, email, password):
        if email in self.students and self.students[email].password == password:
            return self.students[email]
        else:
            return None

def main():
    sms = StudentManagementSystem()

    while True:
        print("1. Register Student")
        print("2. Login Student")
        print("3. Register Course")
        print("4. Update Grade")
        print("5. Mark Attendance")
        print("6. Display Student Info")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            sms.register_student(name, email, password)
        elif choice == "2":
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            student = sms.login_student(email, password)
            if student:
                print("Login successful!")
            else:
                print("Invalid email or password.")
        elif choice == "3":
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            student = sms.login_student(email, password)
            if student:
                course_name = input("Enter course name: ")
                student.register_course(course_name)
                print(f"Course '{course_name}' registered successfully!")
            else:
                print("Invalid email or password.")
        elif choice == "4":
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            student = sms.login_student(email, password)
            if student:
                course_name = input("Enter course name: ")
                grade = input("Enter grade: ")
                student.update_grade(course_name, grade)
                print(f"Grade for course '{course_name}' updated to {grade}.")
            else:
                print("Invalid email or password.")
        elif choice == "5":
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            student = sms.login_student(email, password)
            if student:
                course_name = input("Enter course name: ")
                student.mark_attendance(course_name)
                print(f"Attendance for course '{course_name}' marked.")
            else:
                print("Invalid email or password.")
        elif choice == "6":
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            student = sms.login_student(email, password)
            if student:
                student.display_info()
            else:
                print("Invalid email or password.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
