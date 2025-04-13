#Classes and objects
#This is a module for student class...WE will call this class in another (main) file
class university:
#parent class

class student(university):
#Inherited class
    def __init__(self, name,dept,gpa, is_on_probation):     #initilizer or also known as a constructor
        self.name=name                                      # (self) is by default and then rest variable are written after that
        self.dept=dept
        self.gpa=gpa
        self.is_on_probation=is_on_probation
