#Pyhton Condition 
a=20
b=30
if b > a:
    print("b is greater than a")


#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  #ELSE
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



if a > b: print("a is greater than b") 

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B") 

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 



a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 20
b = 33
if not a > b :
  print("a is not grater than b")

#Nested IF
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 

#Pass statement

a = 33
b = 200

if b > a:
  pass
  print("checl")     

pass 
if b > a:
  print("hey fun")             