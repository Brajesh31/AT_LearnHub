def func():
    print("Hello worls")

func()

#argument
def multiple_of_two(n):
    if(n%2==0):
        print("{} is multiple of two".format(n))
    else:
        print("{} is not a multiple of two".format(n))

multiple_of_two(98)
multiple_of_two(99)

def name(fname,lname):
    print(fname+" "+lname)
name("Akshay","Tripathi")




def fruits(*fruits):
        for i in fruits: 
         print("fruit "+ i)

fruits("apple", "mango", "cherry")

def person_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# Using keyword arguments to pass values
person_info(name="Askshay",
             age=22, city="Raebareli")




def print_info(**person):
    for key, value in person.items():
        print(key + ": " + value)

# Using arbitrary keyword arguments 
# to pass values
print_info(name="Akshay", age="22")
print_info(name="Sam", age="21", 
           city="Sultanpur", 
           occupation="Sultnpur")


def country(country="India"):
    print(country)

country()
country("Australia")

def name(name):
    for letter in name:
        print(letter,end=" ")
name("Akshay")
print()



#Factoral
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the factorial function
print(factorial(5))  # Output: 120
print(factorial(6))  # Output: 720

#Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the Fibonacci function
print(fibonacci(5))  # Output: 5
print(fibonacci(6))  # Output: 8

#sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Test the sum_of_digits function
print(sum_of_digits(12345))  # Output: 15 (1 + 2 + 3 + 4 + 5)

#Binary Search
def binary_search(arr,target,low,high):
    if low <= high:
        mid=(low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr,target, mid+1,high)
        else:
            return binary_search(arr,target,low,mid-1)
        
    return -1
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search(arr, target, 0, len(arr) - 1))  # Output: 3 (index of target 7)




x = lambda a : a + 10
print(x(5)) 

x = lambda a,b : a * b
print(x(5,9))

x = lambda a,b,c: a + b+c+10
print(x(5,3,4)) 





def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))






def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))




def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)) 




cars = ["Ford", "Volvo", "BMW"] 

#Lambda Function or Anonymous Function
#  : also known as one liner function

def minus(a,b):
    return a-b 
print(minus(9,2))

subtract = lambda a,b : a-b
print(subtract(9,2))

#list of lis
a=[[1,3],[2,10],[5,8]]
a.sort(key= lambda   :a[1] )
