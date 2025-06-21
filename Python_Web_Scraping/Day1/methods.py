class Student:
    
    school= "Shorthills"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    #self means instance variable
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1= value
    
    @classmethod
    def info(cls):
        return cls.school
    
    @staticmethod
    def information():
        print("This is student class")

Student.information()

s1=Student(12,34,56)  
s2=Student(23,67,97)

print(s1.avg())
print(s2.avg())

print(Student.info())


#avg is instance method 
# because it works with an object