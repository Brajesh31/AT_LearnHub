class Student:

    def __init__(self,name,rollno):
        self.name= name
        self.rollno=rollno
        self.lap = self.laptop()

    
    def show(self):
        print(self.name, self.rollno)
    
    class laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "I5"
            self.ram = 16


s1 = Student('Akshay' ,10)
s2 = Student("Saumya", 50)

lap1= s1.lap
lap2= s2.lap
s1.show()
print(id(lap1))  