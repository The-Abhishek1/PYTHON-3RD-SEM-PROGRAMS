# Define a base class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Define a derived class called Employee
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

# Create an instance of the Employee class
employee = Employee("John Doe", 30, 12345)

# Call the display_info method of the Employee class
employee.display_info()
