class Student:
    
    stuCount = 0

    def __init__(self):  
          
    
        self.name = input('enter student name:')
        self.rollno = input('enter student rollno:')
        Student.stuCount += 1
  
    
    def displayStudent(self):  
        print("Name:", self.name, "Rollno:", self.rollno)
  
  
stu1 = Student()
stu2 = Student()
stu3 = Student()
