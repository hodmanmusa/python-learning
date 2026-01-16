# --------------------------------------------------
# Python Dunder / Magic Methods
# --------------------------------------------------

class Employee:
    # Class variable shared by all employees
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def full_name(self):
        # Return full name of employee
        return f"{self.first} {self.last}"

    def apply_raise(self):
        # Apply salary raise
        self.pay = int(self.pay * self.raise_amount)

    # ---------------- Dunder Methods ----------------

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def __add__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


# --------------------------------------------------
# Using the class and its methods (Tests)
# --------------------------------------------------

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)

# String representations (preferred usage)
print(emp_1)            # Calls __str__()
print(repr(emp_1))      # Calls __repr__()

# Salary raise
print("Before raise:", emp_1.pay)
emp_1.apply_raise()
print("After raise:", emp_1.pay)

# Using __add__
print("Total salary:", emp_1 + emp_2)

# Using __len__
print("Name length:", len(emp_1))

# Built-in dunder method equivalents (for learning)
print(1 + 2)
print(int.__add__(1, 2))

print("a" + "b")
print(str.__add__("a", "b"))

print(len("test"))
print(str.__len__("test"))
