#String Format

a=22
n='akshay{}'
print(n.format(a))

#we can use indexing
a=1
b=2
c=3
f='fruits: cherry {2} apple {0} banana {1}'
print(f.format(a,b,c))

#without indexing
f='fruits: cherry {} apple {} banana {}'
print(f.format(a,b,c))
