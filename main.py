#==== Student Class with Getters, Setters, and and Merhods====

class Student:
    def __init__(self, name, roll_no, course):
        self._name = name
        self._roll_no = roll_no
        self._course = course

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        self._name = value

    # Getter for roll_no
    @property
    def roll_no(self):
        return self._roll_no

    # Setter for roll_no
    @roll_no.setter
    def roll_no(self, value):
        self._roll_no = value

    # Getter for course
    @property
    def course(self):
        return self._course

    # Setter for course
    @course.setter
    def course(self, value):
        self._course = value

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")
        print("-------------------------------")

    def update_info(self, new_roll_no=None, new_course=None):
        if new_roll_no:
            self.roll_no = new_roll_no
        if new_course:
            self.course = new_course

#====Global List to Store Students====

students = []

#====Helper Functions====

def add_student():
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    student = Student(name, roll_no, course)
    students.append(student)
    print(f"\n Student '{name}' added successfully.\n")

def view_students():
    if not students:
        print("\nNo students available.\n")
    else:
        print("\n List of Students:")
        for student in students:
            student.display_info()

def update_student():
    roll_no = input("Enter roll number to update: ")
    for student in students:
        if student.roll_no == roll_no:
            new_roll = input("Enter new roll number (press Enter to skip): ")
            new_course = input("Enter new course (press Enter to skip): ")
            student.update_info(new_roll if new_roll else None, new_course if new_course else None)
            print("\n Student updated.\n")
            return
    print("\n Student not found.\n")

def search_student():
    keyword = input("Enter name or roll number to search: ")
    for student in students:
        if student.name.lower() == keyword.lower() or student.roll_no == keyword:
            print("\n Student Found:")
            student.display_info()
            return
    print("\n No student found.\n")

def delete_student():
    keyword = input("Enter name or roll number to delete: ")
    for student in students:
        if student.name.lower() == keyword.lower() or student.roll_no == keyword:
            students.remove(student)
            print(f"\n Student '{student.name}' deleted.\n")
            return
    print("\n Student not found.\n")

# ===== Menu Loop =====

while True:
    print("\n===== Student Management Menu =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        search_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print(" Exiting the program. Goodbye!")
        break
    else:
        print(" Invalid choice. Please try again.")



