l=['a','k','s','h','a','y']
print(len(l))
print(l[4])
l[4]='k'
print(l)
l[4]='a'

l=['aks',22,31.90]
print(l,type(l))

#list constructor to make list 
l=list(("aks",31,2000.78))
print(l,type(l))


#Accessing List Items
l=['a','k','s','h','a','y']
print(l[3])
print(l[-1])
print(l[2:4])
print(l[:4])
print(l[2:])
print(l[-2:-4])
print(l[-4:-2])

#Check if
if 's' in l:
    print('s present')

#Change List Items
l=['a','k','s','h','a','y']
l[4]='m'
print(l)

#changing range of items
l[1:3]=['j','p']
print(l)

#if inserted more then that item will add there
l[1:3]=['q','r','f','g']
print(l)

#if inserted less items
l[1:3]=['d']
print(l)

#insert(index, value)
l.insert(2,22)
print(l)




##ADD LIST ITEMS
l=['a','k','s','h','a','y']

#append()
l.append('t')
print(l)
#insert()
l.insert(2,'l')
print(l)
#extend()
t=['t','r','i','p','a','t','h','i']
l.extend(t)
print(l)

l=['a','k','s','h','a','y']
tup=('q','r','l')
l.extend(tup)
print(l)

#Remove Lit Items
l=['a','k','s','h','a','y']
l.remove('s')
print(l)

l=['a','k','s','h','a','y']
l.pop(1)
print(l)

l=['a','k','s','h','a','y']
l.pop()
print(l)

l=['a','k','s','h','a','y']
del l[3]
print(l)

l=['a','k','s','h','a','y']
del l  # will delete complete list
#print(l)

l=['a','k','s','h','a','y']
l.clear()
print(l)


#LOOP LIST
l=['a','k','s','h','a','y']

for x in l:
    print(x+" ",end="")
print('\n')

for i in range(len(l)):
    print(l[i]+" ",end="")
print('\n')

i=0
while i< len(l):
    print(l[i],end='')
    i=i+1

print('\n')


#Sort List Ascending 
l=['a','k','s','h','a','y']
l.sort()
print(l)
n=[8,5,3,8,3,665,32,65,6]
n.sort()
print(n)

#Descending
l.sort(reverse=True)
print(l)
n.sort(reverse=True)
print(n)

#Customized Sort
def func(x):
    return (x-9)
n.sort(key=func)
print(n)

#Case Sensitive Sort
l=['a','A','b','Z','J','g']
l.sort()
print(l)

#Case insensitive Sort
l.sort(key=str.lower)
print("CASE INSENSITIVEE")
print(l)
l.sort(key=str.upper)
print(l)

l=['a','A','b','Z','J','g']
l.reverse()
print(l)

#Copy a String
l=['a','A','b','Z','J','g']

l2=l.copy()
print(l2)
print(id(l2),id(l))

l3=list(l)
print(l3)
print(id(l), id(l2), id(l3))

#Join Two List
l1=['a','b','c']
l2=['k','g','e']
l3=l1+l2
print(l3)

#using append()
for x in l2:
    l1.append(x)
print(l1)  

#using extend
l1.extend(l2)
print(l1)

#count()

l=['a','k','s','h','a','y']
print(l.count('a'))

#unpacking List

l=['a','k','s','h','a','y']
a,b,c,d,e,f=l
print(a,b,c,d,e,f)

#negative indexing:

l=['a','k','s','h','a','y']
print(l[-2])

#list slicing
print(l[2:5])
print(l[-5:])

l.insert(2,['q','t','y','h','d'])
print(l)

l=['a','k','s','h','a','y']
l.append(l)
print(l)


l=['a','k','s','h','a','y']
l.extend(l)
print(l)

x=5

def func():
  global x
  x=3
  print(x)

func()
print(x)  

print(type(x))

x=3
x=float(True)
print(type(x))

l=['a','k','s']
l2=['h','a','y']
l.append(l2)
print(l)
