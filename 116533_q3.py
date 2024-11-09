"""
Question 3: Employee and Department Management (10 marks)
Scenario: You’re designing a basic system to manage employees and departments in a
company
"""
# Class for Employee
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary:.2f}")
    
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to ${self.salary:.2f}")


# Class for Department
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store Employee objects
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added employee {employee.name} (ID: {employee.employee_id}) to department '{self.department_name}'.")

    def total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for '{self.department_name}' department: ${total_salary:.2f}")
        return total_salary

    def display_all_employees(self):
        if not self.employees:
            print(f"No employees in department '{self.department_name}'.")
            return
        print(f"\nEmployees in '{self.department_name}' department:")
        for employee in self.employees:
            employee.display_details()


# Interactive Code for Department Management
def main():
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nDepartment Management Menu:")
        print("1. Add Employee to Department")
        print("2. Update Employee Salary")
        print("3. Display All Employees")
        print("4. Display Total Salary Expenditure")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the employee's name: ")
            employee_id = input("Enter the employee's ID: ")
            try:
                salary = float(input("Enter the employee's salary: "))
                employee = Employee(name, employee_id, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid salary entered. Please enter a numeric value.")

        elif choice == "2":
            employee_id = input("Enter the employee's ID to update salary: ")
            employee = next((e for e in department.employees if e.employee_id == employee_id), None)
            if employee:
                try:
                    new_salary = float(input("Enter the new salary: "))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid salary entered. Please enter a numeric value.")
            else:
                print("Employee not found in the department.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.total_salary_expenditure()

        elif choice == "5":
            print("Exiting the department management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the interactive code
main()
