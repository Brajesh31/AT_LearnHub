class A:
    def func1(self):
        print("FUN1 is ")

    def func2(self):
        print("FUN2 is ")

class B:
    def func3(self):
        print("FUN3 is ")

    def func4(self):
        print("FUN4 is ")

class C(A,B):
    def func5(self):
        print("fun5 is ")
a1=A()
a1.func1()
a1.func2()

# b1=B()
# b1.func1()
# b1.func2()
# b1.func3()
# b1.func4()

c1=C()
c1.func1()