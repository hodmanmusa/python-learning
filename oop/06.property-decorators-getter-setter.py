
class Employee:

    raise_amount = 1.04
    num_of_emp = 0 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        # Update class variable when a new employee is created
        Employee.num_of_emp += 1
    
    @property
    def email(self): 
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @fullname.setter
    def fullname(self, name): 
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self): 
        print('Delete Name!')
        self.first = None
        self.last = None 
    

emp_1 = Employee('Musa', 'Hodman', 500_000)
emp_2 = Employee('Wais', 'Zafari', 600_000)
emp_3 = Employee('Najib', 'Zafari', 700_000)

emp_1.first = "Hemat"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Musa Hodman'

print(emp_1.fullname)

del emp_1.fullname