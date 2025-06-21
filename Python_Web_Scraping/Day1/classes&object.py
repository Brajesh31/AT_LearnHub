
class Computer:

    def __init__(self, CPU, RAM):
        self.CPU=CPU
        self.RAM=RAM
        print("in init")

    def config(self):
        print("Config is ",self.CPU,self.RAM)



comp1 = Computer("i5",16)
comp2 = Computer("Rayzen 3",8)
print(type(comp1))

Computer.config(comp1)
Computer.config(comp2)

comp1.config()
comp2.config()

 