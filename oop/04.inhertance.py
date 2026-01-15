# --------------------------------------------------
# Inheritance and Subclasses Example
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

    def fullname(self):
        # Returns full name of employee
        return self.first + ' ' + self.last

    def apply_raise(self):
        # Applies salary raise
        self.pay = self.pay * self.raise_amount


class Developer(Employee):
    # Developers have a higher raise
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Initialize Employee attributes
        super().__init__(first, last, pay)
        # Developer-specific attribute
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Avoid mutable default argument
        self.employees = employees if employees else []

    def add_emp(self, emp):
        # Adds employee if not already managed
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        # Removes employee if managed
        if emp in self.employees:
            self.employees.remove(emp)

    def diplay_emps(self):
        # Displays all managed employees
        for emp in self.employees:
            print('-->', emp.fullname())


# --------------------------------------------------
# Testing the classes
# --------------------------------------------------

# Creating objects
emp_dev1 = Developer('Musa', 'Hodman', 800000, 'Java')
emp_dev2 = Developer('Farhad', 'Zafari', 900000, 'Python')
emp_mgr = Manager('Najib', 'Zafari', 600000, [emp_dev1])

# Testing inherited attributes and methods
print(emp_dev1.email)       # Test email generation
print(emp_mgr.fullname())   # Test inherited fullname method
print(emp_dev2.pay)         # Test initial pay

# Testing raise for Developer (10%)
emp_dev2.apply_raise()
print(emp_dev2.pay)         # Pay after raise
print(emp_dev2.prog_lang)   # Developer-specific attribute

# Testing raise for Manager (4%)
emp_mgr.apply_raise()
print(emp_mgr.pay)  # Pay after raise

# Testing Manager employee management
emp_mgr.diplay_emps()       # Initial managed employees
emp_mgr.add_emp(emp_dev2)
emp_mgr.diplay_emps()       # After adding employee
emp_mgr.remove_emp(emp_dev2)
emp_mgr.diplay_emps()       # After removing employee

# Testing isinstance()
print(isinstance(emp_mgr, Manager))    # True
print(isinstance(emp_mgr, Employee))   # True
print(isinstance(emp_mgr, Developer))  # False

# Testing issubclass()
print(issubclass(Developer, Employee)) # True
print(issubclass(Manager, Employee))   # True
print(issubclass(Manager, Developer))  # False
