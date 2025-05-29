# def addition(a,b):
#     print(a+b)
#
# addition(2,3)

# def employee(name, salary =500000):
#     print("Name :" , name)
#     print("Salary :", salary)
#
# employee("Nitin", 2000000)
# employee("Nitin")

# def addition(a,b,c):
#     print(a+b-c)
#
# addition(c=10, a=2, b=3)   #keyword parameter

# Arbitary number of  position argument
# def a(c,a,*b):
#     print(sum((b)))
#     print(a+c+(b))
#
# a(1,2,3,4,5)


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd
# def lesser_of_two_number(a,b):
#     if a % 2 ==0 and b %2 == 0:
#         print(min(a,b))
#     else:
#         if a % 2 !=0 or b % 2 !=0:
#             print(max(a,b))
#
# lesser_of_two_number(13, 21)

# ----------------------------------------------------------------------

#  Write a function takes a two-word string and
# returns True if both words begin with same letter

# def comparison(lst):
#     first =lst.split()
#     if first[0][0] == first[1][0]:
#         print('Matched')
#     else:
#         print('Not Matched')
#
# comparison('Navi Numbai')

# def find_max(lst):
#
#     max = 0
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print(find_max([1, 2, 99, 4]))

# def factorial(n):
#     fact =1
#     for num in range(2,n+1):
#         fact =fact*num
#     return fact
#
# print(factorial(4))

# Lambda function
# s = lambda x : x ** 3
# print(s(2))

# def double(x):
#     return x*2
#
# lst = [2,4,6,12,10]
# l1 = []
# for i in lst:
#     l1.append(double(i))
#
# print(l1)

# Map function
# def double(x):
#     return x*2
#
# l1 = [2, 5, 12, 44, 22]
#
# lst = list(map(double , l1))
# print(lst)

# lst = [2,3,5,6,12,44,56,79.83,32,12,11,9,24]
# ls = list(filter(lambda x : x % 2 == 0, lst))
# print(ls)

#lst =['v', 'r', 'a', 'h', 'e', 'o', 'i']
#ls = list(filter(lambda x : x[0] in 'eaiou' , lst ))
#print(ls)

class circle():
   def __init__(self, radius):
       self.radius = radius

   def area(self):
       return self.radius**2*3.14

   def circumference(self):
       return self.radius*2*3.14


result = circle(2)
print("Area"  ,result.area())
print("Circumference", result.circumference())

# class rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#         def area(self):
#             return self.length * self.width
#
#         def perimeter(self):


