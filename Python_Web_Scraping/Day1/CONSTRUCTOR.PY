
class Computer:
    
    def __init__(self):
        self.name="Akshay"
        self.age=22

    def update(self):
        self.age= 30
    
    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False

c1=Computer()
c2=Computer()

c1.update()

# if c1 == c2 :
#     print("Objects are equal")

if c1.compare(c2):
    print("Objects are equal")
else:
    print("They are different")

