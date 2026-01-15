# --------------------------------------------------
# Class methods, static methods, and instance methods
# --------------------------------------------------

class Employee:

    # Class variables shared by all instances
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        # Increment employee count
        Employee.num_of_emp += 1

    def fullname(self):
        # Returns full name of the employee
        return self.first + ' ' + self.last

    def apply_raise(self):
        # Applies raise using class or instance raise_amount
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        # Updates raise amount for the class
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # Alternative constructor using a string
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        # Checks if a given date is a workday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Creating employee objects
emp_1 = Employee('Musa', 'Hodman', 500000)
emp_2 = Employee('Wais', 'Zafari', 600000)
emp_3 = Employee('Najib', 'Zafari', 700000)

# Using class method to change raise amount
Employee.set_raise_amt(1.05)

# Accessing class variable from class and instances
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Strings representing employee data
emp_str_1 = 'Jhon-Deo-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Creating objects normally and via class method
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
new_emp_2 = Employee.from_string(emp_str_2)

# Printing employee details
print(new_emp_1.email)
print(new_emp_2.email)
print(new_emp_2.pay)

# Using static method
import datetime
my_date = datetime.date(2026, 1, 17)

print(my_date.weekday())
print(Employee.is_workday(my_date))
