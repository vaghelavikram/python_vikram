class Employee:
    company = "camal"
    sallary = 500
    location = "kolkata"

def changeSallary(self,sal):
    self.__class__.sallary = sal



e = Employee()
print(e.sallary)
e.changeSallary(500)
print(e.sallary)
print(Employee.sallary)
