#Tuple
name=('a','k','s','h','a','y')
#allow duplicates
print(name)

#Tuple Items
print(name[1])
print(name[-1])

print(len(name))#tuple lenght

#create tuple with single item
tup=('akshay',)
print(type(tup)) #type()

#tuple items could be of any type
tup=(23,'akshay',7.5,True,)

#tuple Constructor: used to make tuple
tup=tuple(('a','k','s'))
print(tup, type(tup))

#Access tuple item
name=('a','k','s','h','a','y')
print(name[2])
print(name[-3]) #negative indexing
print(name[2:5]) #ranges of index
print(name[:5])
print(name[2:])
print(name[-4:-1])
if 's' in name:
    print("s is present") 

#Update Tuple

#updating tuple element
name=('a','k','s','h','a','y')
l=list(name)
l[1]='q' 
name=tuple(l)
print(name)


name=('a','k','s','h','a','y')
l=list(name)
l[1]=('q','r','t') #adding tuple to tuple
name=tuple(l)
print(name)


name=('a','k','s','h','a','y')
l=list(name)
l[1]=['q','r','t'] #adding list to tuple
name=tuple(l)
print(name)

#ADD element to tuple
name=('a','k','s','h','a','y')
l=list(name)
l.append('t') #append element
name=tuple(l)
print(name)
#Add tuple to tuple
name=('a','k','s','h','a','y')
surname=('t','r','i','p','a','t','h','i')
name += surname
print(name)
name=('a','k','s','h','a','y')
name =name*2
print(name)

#Remove element from tuple
name=('a','k','s','h','a','y')
l=list(name)
l.remove('a') #it will remove the first encountered 'a'
name=tuple(l)
print(name)

del name
#print(name) will throw error

#UNPACK TUPLES
name=('ram','lakshman','bharat','shatrughan')
(n1,n2,n3,n4)=name
print(n1 ,n2 ,n3,n4)
(n1,*n2)=name #Using Asterisk
print(n1)
print(n2)
(*n1,n2,n3)=name
print(n1)
print(n2,n3)

#Looping in Tuple
#ForLoop
name=('a','k','s','h','a','y')
for letter in name:
    print(letter, end="")
print("")
for i in range(len(name)):
    print(name[i],end=" ")
print("")

for i in range(2,len(name)):
    print(name[i],end=" ")
print("")

#While Loop
name=('a','k','s','h','a','y')
i=0
while i<len(name):
    print(name[i])
    i=i+1

#Join Tuple
name=('a','k','s','h','a','y')
surname=('t','r','i','p','a','t','h','i')
fullName=name+surname
print(fullName)

#Multiply Tuple
tup=name*2
print(tup)

#Tuple Method
name=('a','k','s','h','a','y')
print(name.count('a'))
print(name.index('h'))



name=('a','k','s','h','a','y')
l=list(name)
l[1:4]=['q','r','t'] #adding tuple to tuple
name=tuple(l)
print(name)

