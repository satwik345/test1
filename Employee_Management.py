class Employee:
    def __init__(self, emp_id, name, age, pay):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.pay = pay

    def show(self):
        print(f"EMPLOYEE ID: {self.emp_id}, NAME: {self.name}, AGE: {self.age}, PAY: {self.pay}")


class Manager:
    def __init__(self):
        self.employees = []

    def add(self, emp_id, name, age, pay):
        emp = Employee(emp_id, name, age, pay)
        self.employees.append(emp)

    def show(self):
        print("\n--- Employee List ---")
        for emp in self.employees:
            emp.show()


m = Manager()
emp_id = input("Enter Employee ID: ")
name = input("Enter Name: ")
age = input("Enter Age: ")
pay = input("Enter Pay: ")
m.add(emp_id, name, age, pay)

while True:
    choice = input("Do you want to ADD an employee? (y/n): ").lower()
    if choice == 'n':
        break
    elif choice == 'y':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        pay = input("Enter Pay: ")
        m.add(emp_id, name, age, pay)
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

m.show()
