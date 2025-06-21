#You can use double or single quotes:

print("Hello")
print('Hello')

#Assign String to a Variable

a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 


#String as Array
a = "Hello, World!"
print(a[1]) 

#Looping in String
for x in "banana":
 print(x)

#Lenght of String
a = "Hello, World!"
print(len(a))   

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Check if
txt = "The best things in life are free!"
if "free" in txt:
 print("Yes, 'free' is present.") 

#Check if not
txt = "The best things in life are free!"
print("expensive" not in txt) 


txt = "The best things in life are free!"
if "expensive" not in txt:
 print("No, 'expensive' is NOT present.")

