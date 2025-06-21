#Arithmatic Operators
x=5
y=9
#ddition 	
print(x + y) 	
#Subtraction 
print(x - y) 	
#Multiplication 
print(x * y) 	
#Division
print(x / y) 	
#Modulus 
print(x % y)	
#	Exponentiation
print(x ** y) 	 	
#Floor division 
print(x // y)

#Assignment Operator
x=5
print(x)
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
x=5
x &= 3
print(x)
x |= 3
print(x)
x ^= 3
print(x)
x >>= 3
print(x)
x <<= 3
print(x)

#Comparision Operator
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical Operator
#AND
x = 5
print(x > 3 and x < 10)
#OR
print(x > 3 or x < 10)
#NOT
print(not(x > 3 and x < 10))

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

m=3
n=4
print(m,n, m is n)
print(m,n , m is not n)
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


#MEMBERSHIP OPERATOR
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
