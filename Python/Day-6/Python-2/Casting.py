#INTEGER 
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

#FLOATS:
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

#String
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)


#Random module
import random
n=random.randint(2,8) # 2<=n<=8
print(n)
n1=random.randrange(2,4)# 2<=n1<4 this will not include 4
print(n1)


l=[10,203,60,78]
e=random.choice(l)
print(e)

r=random.random()
print(r)

l=[10,20,30,40]
random.shuffle(l)
print(l)

f=random.uniform(2,3)
print(f)

#Type Casting

name=input("Enter you name: ")
print(tuple(name))
print(list(name))
#print(dict(name))
print(set(name))