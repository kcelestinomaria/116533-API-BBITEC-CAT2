"""
Question 2: Online Course Management (10 marks)
Scenario: You’re designing a system to manage an online course, allowing instructors to
manage students and assignments.
"""
# Class for Student
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Stores assignment names and corresponding grades
    
    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")
    
    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name} (ID: {self.student_id}):")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print(f"No grades available for {self.name}.")


# Class for Instructor
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List of Student objects enrolled in the course
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} (ID: {student.student_id}) to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
            print(f"Assigned grade {grade} for '{assignment_name}' to {student.name} (ID: {student.student_id}).")
        else:
            print(f"Student with ID {student_id} not found in course '{self.course_name}'.")
    
    def display_all_students_grades(self):
        print(f"\nGrades for all students in {self.course_name}:")
        if not self.students:
            print("No students are enrolled in this course.")
            return
        
        for student in self.students:
            student.display_grades()
            print("-" * 30)  # Separator for better readability


# Interactive Code for Instructor
def main():
    # Create an instructor for a course
    instructor = Instructor("Dr. Smith", "Intro to Programming")

    while True:
        print("\nCourse Management Menu:")
        print("1. Add Student to Course")
        print("2. Assign Grade to Student")
        print("3. Display All Students' Grades")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the student's name: ")
            student_id = input("Enter the student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter the student's ID: ")
            assignment_name = input("Enter the assignment name: ")
            try:
                grade = float(input("Enter the grade for the assignment: "))
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid grade entered. Please enter a numeric value.")

        elif choice == "3":
            instructor.display_all_students_grades()

        elif choice == "4":
            print("Exiting the course management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the interactive code
main()
