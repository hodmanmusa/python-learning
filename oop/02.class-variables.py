# --------------------------------------------------
# Working with Classes and Objects in Python (Basics)
# --------------------------------------------------

class Employee:

    # Class variables (shared by all employees)
    raise_amount = 1.04      # Default raise factor (4%)
    num_of_emp = 0           # Counts how many Employee objects are created

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        # Update class variable when a new employee is created
        Employee.num_of_emp += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        """
        Applies a salary raise to the employee.
        Uses self.raise_amount so that instance-level overrides
        (if any) are respected.
        """
        self.pay = self.pay * self.raise_amount


emp_1 = Employee('Musa', 'Hodman', 500_000)
emp_2 = Employee('Wais', 'Zafari', 600_000)
emp_3 = Employee('Najib', 'Zafari', 700_000)


# __dict__ shows only instance variables (not class variables)
print("emp_1 instance attributes:")
print(emp_1.__dict__)
print()

# Accessing class variables via instances and the class
print("Accessing raise_amount:")
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print()

# Inspecting Class Attributes
print("Employee class attributes:")
print(Employee.__dict__)
print()

# Updating a Class Variable (Affects All Instances)

Employee.raise_amount = 1.05  # 5% raise for all employees

print("After updating class raise_amount:")
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print()

# Overriding Class Variable for a Single Instance

# Before overriding, emp_2 has no raise_amount in its own __dict__
print("emp_2 attributes before override:")
print(emp_2.__dict__)
print()

# This creates an instance variable for emp_2 only
emp_2.raise_amount = 1.06  # 6% raise only for emp_2

print("After overriding raise_amount for emp_2:")
print(emp_1.raise_amount)      # Uses class value
print(emp_2.raise_amount)      # Uses instance value
print(Employee.raise_amount)   # Class value remains unchanged