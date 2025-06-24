# # Module 2
# #1 IF
# if True:
#     print("bhavan")

# #2 IF-ELSe
# if True:
#     print("adarsh")
# else:
#     print("Bhavan noob")

# #3 IF-ELIF-ELSe
# a,b=3,5
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# else:
#     print("noob")

# #4 IF-ELIF

# if a<b:
#     print(a)
# elif b>a:
#     print(b)

# check if it is a valid combo
# for every if,else elif block indintation must be at same level
# at any point, only block will be executed in a given combo


#16-6-25   Functions 

#17-6-25 Local vs Global Variable
#18-6-25
# ✅ What is isinstance() in Python?
# isinstance() is a built-in Python function used to check whether an 
# object is an instance of a particular type (or class).
# print(isinstance(5, int))             # True
# print(isinstance(5.0, float))         # True
# print(isinstance("hello", str))       # True
# print(isinstance([1, 2], list))       # True
# print(isinstance(5, float))           # False

def q(*b):
     return sum(b)
a=[1,2,3,3,4]
print(q(a))
# 🧠 What sum() expects:
# The sum() function adds items in an iterable from left to right using +.

# By default:

# sum([1, 2, 3]) → (((1 + 2) + 3)) → 6
# So it tries to do:

# total = 0
# for value in ([1, 2, 3, 3, 4],):
#     total += value
# This becomes:

# total = 0
# total += [1, 2, 3, 3, 4]  # ❌ Error!
# ❌ Why is this an error?
# You're trying to do:

# 0 + [1, 2, 3, 3, 4]
# 0 is an integer

# [1, 2, 3, 3, 4] is a list

# And you can’t add a list to an integer, so Python gives this error:

# TypeError: unsupported operand type(s) for +: 'int' and 'list'

#19-6-25 
#For loops

#20-6-25
#Quiz
#nested loops


#23-6-25
#Assigned Teams
#Given first Project 

#24-6-25
# class AC:

#     def __init__(self, brand, color):

#         self.brand = brand

#         self.color = color

#     def turn_on(self):

#         print(f"Turning on {self.brand} AC...")

#     def turn_off(self):

#         print("Turning off AC...")

# ac = AC('samsung', 'white')

# ac.brand = 'LG'

# ac2 = AC('HAIER', 'white')

# print(ac2.brand)
 
    

 