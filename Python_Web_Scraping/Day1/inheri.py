class A:

    def __init__(self):
        print("in A init")
    def func1(self):
        print("FUN1 is ")

    def func2(self):
        print("FUN2 is ")

class B(A):
    
    def __init__(self):
        super().__init__()
        print("in B init")
    def func3(self):
        print("FUN3 is ")

    def func4(self):
        print("FUN4 is ")

a1=A()
a1 = B()
