# Author: Ryan (AMDG) 10/1/21

r = int(input("enter the radius: "))
h = int(input("enter the hight: "))

#volume
v = 3.14 * (r ** 2) * h
print(v)

#surface area
s = ((2 * 3.14) * r * h) + ((2 * 3.14) * (r ** 2))
print(s)
