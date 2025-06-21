thisdict =	{
  "name": "Akshay",
  "age": 22,
  "year": 2001
}
print(thisdict)
print(thisdict["year"])

#duplicates are not allowed
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "age": 22,
  "year": 2001
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

thisdict = dict(name = "aksahy", age = 22, country = "Gurgaon")
print(thisdict)

#Access Dictionary Item
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "year": 2001
}
print(thisdict)
print(thisdict["year"])
#get method
x=thisdict.get("age")
print(x)
x=thisdict.keys()
print(x)
thisdict["game"]="Asphalt"
print(x)

x=thisdict.values()
print(x)
thisdict["food"]="paratha"
print(x)

thisdict["food"]="dosa"
print(x)

thisdict =	{
  "name": "Akshay",
  "age": 22,
  "age": 22,
  "year": 2001
}
x=thisdict.items()
print(x)
thisdict["game"]="Asphalt"
print(x)
if 'name' in thisdict:
    print(thisdict['name'])


#CHANGE THE DICT
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "game": "NFS",
  "food": "paratha",
  "year": 2001
}
thisdict["game"]="Asphalt"
print(thisdict)

#Update Method
thisdict.update({"food":"maggie"})
print(thisdict)


#ADD to THE DICT
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "year": 2001
}
print(thisdict)
thisdict["game"]="Asphalt"
print(thisdict)

#Update Method
thisdict.update({"food":"maggie"})
print(thisdict)

#REMOVE ITEMS FROM DICT
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "game": "NFS",
  "food": "paratha",
  "year": 2001
}
thisdict.pop("age")
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict
#print(thisdict) show error

#LOOPING
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "game": "NFS",
  "food": "paratha",
  "year": 2001
}
#print keys
for x in thisdict:
  print(x)

#print values
for x in thisdict:
  print(thisdict[x])

#LOOPING with values & keys
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "game": "NFS",
  "food": "paratha",
  "year": 2001
}
#print keys
for x in thisdict.values():
  print(x, end=" ") 
print("")
#print values
for x in thisdict.keys():
  print(thisdict[x],end=" ")
print("")


thisdict =	{
  "name": "Akshay",
  "age": 22,
  "game": "NFS",
  "food": "paratha",
  "year": 2001
}
for x, y in thisdict.items():
  print(x, y) 

#copy dictionary
thisdict =	{
  "name": "Akshay",
  "age": 22,
  "year": 2001
}
mydict = thisdict.copy()
print(mydict)

mydict2 = dict(thisdict)
print(mydict2) 



# Creating a nested dictionary
nested_dict = {
    'person1': {
        'name': 'Akahsy',
        'age': 22,
        'email': 'akahay@email.com'
    },
    'person2': {
        'name': 'sam',
        'age': 22,
        'email': 'sam@email.com'
    }
    }


# Accessing nested dictionary values
print(nested_dict['person1']['name'])           # Output: 'Alice'
# Adding a new entry to the nested dictionary
nested_dict['person2']['phone'] = '555-1234'
# Modifying a value in the nested dictionary
nested_dict['person1']['age'] = 31
# Deleting an entry in the nested dictionary
del nested_dict['person2']['email']
# Printing the entire nested dictionary
print(nested_dict)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 


thisdict =	{
  "name": "Akshay",
  "age": 22,
  "age": 21,
  "year": 2001
}
print(thisdict)

thisdict =	{
  "name": "Akshay",
  "age": 22,
  "year": 2001
}

for x,y in thisdict.items():
    print(x,y)