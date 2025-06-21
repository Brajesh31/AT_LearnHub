#While Loop
i = 1
while i <= 10:
  print(i*2)
  i += 1
  if(i%2==0):continue

#break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 


#continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    print("Skipping iteration 3")
    continue
  print(i)  



#using esle with while
i=1
while i<4:
  print(i)
  i+=1
else:
  print("out of loop")


#FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#looping through strings
for x in "banana":
  print(x,end=" ")
print()

print("print before break")
num = [1, 3, 2]
for x in num:
  print(x)
  if(x==3):
    break
print("print after break") 
num= [1, 3, 2]
for x in num:
  if(x==3):
    break
  print(x)

name=['a','k','s','h','a','y']
for letter in range(2,len(name)):
  if(name[letter] =='a'):
    continue
  print(name[letter])


name=['a','k','s','h','a','y']
for letter in range(1,len(name),2):
  print(name[letter])


#Else in For loop
for x in range(6):
  print(x)
else:
  print("Finally finished!") 

#The else block will NOT be executed if 
#the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

for x in [0, 1, 2]:
  pass