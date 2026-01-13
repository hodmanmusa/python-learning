# Working with classes and objects in Python(The Basics)


class Employee: 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self): 
        return self.first + ' ' + self.last
    
emp_1 = Employee('Musa', 'Hodman', 500000)
emp_2 = Employee('Wais', 'Zafari', 600000)
emp_3 = Employee('Najib', 'Zafari', 700000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

emp3_fullname = Employee.fullname(emp_3)
print(emp3_fullname)