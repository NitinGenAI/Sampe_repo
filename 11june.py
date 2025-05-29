s1 = {12,4,34,89,56,12,845,11}
print(s1)
s1.add(29)
print(s1)
s1.remove(4)
print(s1)
s2 = {65,66,67}
s2.update(s1)
print(s2)
#s2.remove(888)
s2.discard(888)
print(len(s2))
print(sorted(s2))
a ={3,4,5,6}
b={9,8,7,6}
c =(a | b)    # ubion - consists of both a and b
print(c)
c =a&b   # intersection - common value between the both a and b
print(c)

c = a - b  # difference - displays value which is in a
print(c)
c = b - a   # difference - displays value which is in b
print(c)
d = a ^ b   # symetric difference  - consist of both a and b excluding common
print(d)
print(a.pop())
 # -- Dictionary --- key : value
d1 = {}
print(type(d1))
d1 = {1 :4 , 2 : 8 , 'k2' : 'nitin' }
print(d1)
d1['k2'] ='sharma'
print(d1['k2'])
print(d1)

#  string
s1 = 'hello brother'
print(s1)
print(s1[4])

print(s1[2:9])