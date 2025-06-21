
#Python Variables
x = 5
y = "Hello, World!"

print(x,y)

#Casting 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

#GET the type 
x = 5
y = "John"
print(type(x))
print(type(y)) 

#Single or Double Quotes
x = "John"
# is the same as
x = 'John'

#Case Sensitive Variables
a = 4
A = "Sally"
#A will not overwrite a 

#Python variables names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#OUTPUT VARIABLES
x = "Python"
y = "is "
z = "awesome"
print(x, y, z)
print(x+y+z)

x = 5
y = 10
print(x + y)

#Global Variable 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

#Global Keyword 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

#changing varible to globla inside function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 


