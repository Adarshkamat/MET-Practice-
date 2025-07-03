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

# def q(*b):
#      return sum(b)
# a=[1,2,3,3,4]
# print(q(a))
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

#25-06-2025
# animals=["cat","dog","monkey"]

# for i,a in enumerate(animals):
#     print(a+animals[(i+1)%len(animals)][0:2])  

#26-6-2025
# class DOG:
#     def __init__(self,name,breed):
#         self.__name=name
#         self.breed=breed
#     def set_dog_name(self,new_name):
#         self.__name=new_name
#     def get(self):
#        print(f"{ self.__name}")
 
# dog1=DOG("luffy","Golden Retriver")
# dog1.set_dog_name("luccy")
# dog1.get()
   
# 1-7-25
# PROJECT PRESENTATION

#2-7-2025
#backend server REST API
# class User:
#     def __init__(self, name, m_id):
#         self.name = name
#         self.id = m_id
#         self.cart = None

# class Product:
#     def __init__(self, p_name, price, quantity):
#         self.p_name = p_name
#         self.price = price
#         self.quantity = quantity

#     def is_available(self, quantity):
#         return self.quantity >= quantity

# class Cart:
#     def __init__(self):
#         self.items = []  # list of tuples: (Product, Quantity)

#     def add_product(self, product, quantity):
#         if product.is_available(quantity):
#             product.quantity -= quantity
#             self.items.append((product, quantity))
#         else:
#             print(f"Only {product.quantity} of {product.p_name} available. Cannot add {quantity}.")

#     def display_cart(self):
#         print("\n--- Cart Contents ---")
#         sum=0
#         for item, qty in self.items:
#             print(f"{item.p_name} - Qty: {qty} - Price per unit: ₹{item.price} ")
#             sum+=item.price*qty
#         print(f"Estimated Total Bill {sum}")
#         print("----------------------\n")

# # # Usage
# # user1 = User("Adarsh", 554)
# # p1 = Product("Chips", 20, 50)
# # p2 = Product("Soap", 30, 10)

# # cart1 = Cart()
# # user1.cart = cart1

# # user1.cart.add_product(p1, 40)  # Adds 40 Chips
# # user1.cart.add_product(p2, 5)   # Adds 5 Soaps
# # user1.cart.display_cart()

# class Student:
#     def __init__(self,name,m1,m2,m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         print(f"The avg is {(self.m1+self.m2+self.m3)/3:.2f}")
# s1=Student("ADARsh",98,86,93)
# s1.avg()

# 3-7-2025
