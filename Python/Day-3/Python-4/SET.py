name={'pan','can','tan'}
print(name,type(name)) #unorder
#duplicates are not allowed, 
#if exist then they automatically remove
name={'pan','can','tan','can'}
print(name,type(name)) 
theset={True,1,0,False,0}
print(theset) #in this true and 1 are consider same
print(len(name)) #length of set

#set constructor
theset=set((True,1,0,False,0))
print(theset,type(theset))


#ACCESS SET ITEMS
name={'pan','can','tan'}
for x in name: 
    print(x)


#Check Set Element
print("can" in name)
print("jan" in name)

#Add Set items
name={'pan','can','tan'}
name.add("jan")
print(name)
newNames={'man','wan','lan'}
name.update(newNames) #adding two set
print(name)
name={'pan','can','tan'}
namelist=['fan','ran','han']
name.update(namelist) #Adding list to set
print(name)

#Remove Item from Set
name={'pan','can','tan','jan','fan','ran','han'}
print(name)
name.remove('jan')
print(name)
#name.remove('ian'): show error
name.discard('tan')
print(name)
#name.remove('ian'): show no error
x=name.pop()
print(x)
print(name)
name.clear()
print(name)
del name
#print(name): show error

#loop Set
name={'pan','can','tan'}
for n in name:
    print(n)


#Join Set
n1={'pan','can','tan'}
n2=['fan','ran','han','pan','can']
print(n1.union(n2))
n1.update(n2)
print(n1)
n1={'pan','can','tan'}
print(n1.intersection(n2))
n1.intersection_update(n2)
print(n1)
n1={'pan','can','tan'}
print(n1.symmetric_difference(n2))
print(n1)
n1={'pan','can','tan'}
n1.symmetric_difference_update(n2)
print(n1)


#SET Method
n1={'pan','can','tan'}
n2=n1.copy()
print(n2, id(n1),id(n2))

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z={"q","r"}
print(x.issubset(y))
print(y.issuperset(x))
print(x.issuperset(y))
print(x.isdisjoint(y))
print(x.isdisjoint(z))
