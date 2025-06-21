#Global variabble and local variable
x="fantastic"

def myfunc():
    x="awesome"
    print(x)

myfunc()

print(x)

#Global keyword and local variable
x="fantastic"


def myfunc():
    global x
    x="awesome"
    print(x)

print(x)

myfunc()

print(x)


#Basic introduction to data types

#1.Number(int,float , complex)
a=5
print(a, type(a))
a=5.5
print(a, type(a))
a=2+7j
print(a,type(a))

#2.String
s1='My'
s2="Name"
s3='''Akshay 
multiline string 
se de saka'''
print(type(s1),type(s2),type(s3)) 
print(s1)
print(s2)
print(s3)

#List-mutable
a=[1,2.2,'ws']
b=[45,'kam',4]
print(a[1])
print(b[1])
a[2]='rtr'
print(a)

print(a, type(a))
a[1]='akshay'
print(a)

#Tuple-immutable
t=(1,'akshay',7.8)
print(t,type(t))
t2=('akshay')
print(t2,type(t2))

#dictionary
d={
    'name': 'akshay',
    1:'value', 
    'key':2
    } 
print(d[1])
print(d, type(d))

#tuple 
s={2,3.4,'aks',2,9.89}
print(s)
print(type(s))

#Variables
a=10
b=10

print(a,b)
print(id(a),id(b))

import math
print(math.acos(0.9))

x=[10]
y=10
print(x is y)
print(x==y)

s="AKSHAY"
print('S' in s)

print(s[:2])
print(s[-9:7])

s="  Akshay Tripathi  "
print(s.upper())
print(s.lower())
print(s.strip())
print(s.split('a'))
s2="I AM CURRENTLY AT SDE1(T)"
print(s+s2)
s2+=' {}'
year=23
print(s+s2.format(year))

s3="My friend \"Ganesha\""
print(s3)
s3="My friend \nGanesha"
print(s3)
s3="My friend l\bGanesha"
print(s3)
s3="My friend \tGanesha"
print(s3)

s3="My friend \"Ganesha\""
# s3[5]='kartikeya'

s3.replace("f","o")
print("Replace "+s3)
s4=s3[:9]+' \"Kartikeya\" & '+s3[9:]
print(s4)


print(bool(0))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(12))

a=5
print(isinstance(a,float))




l=['a','k','s','h','a','y']

i=0
while i in range(len(l)):
    print(l[i],end="")
    i=i+1
print("\n")
for i in l:
    print(i,end="")


print("\n")

m=['h','k']

print(l+l)
l.extend(m)
print(l)


for i in l:
    l.append(i)
print(l)    

s="aksj"
l=list(s)
print(l)


import random
print(random.randint(10,20))
print(random.uniform(10,20))
print(random.randrange(10,20))
l=['a','c','e']
random.shuffle(l)
print(l)