# n="Akshay"
# n[0]='B'

n="Akshay"
n2="B"+n[1:]
print(n2)

print(id(n),id(n2)) # n and n2 are different

n1="Akshay"
print(id(n), id(n1))