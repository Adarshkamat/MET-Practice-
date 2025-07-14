# #1
# a,b=5,7
# if a > b:
#     print(f"{a} is greater")
# else:
#     print(f"{b} is greater")

# #2
# a,b,c=5,4,22
# if a > b and a > c :
#     print(f"{a} is greater")
# elif b > c and b > a :
#     print(f"{b} is greater")
# else:
#     print(f"{c} is greater")

# #3
# a=int(input("Enter a no :"))
# if a>0:
#     print(f"{a} is positive")
# elif a==0:
#     print("It is Zero")
# else:
#     print(f"{a} is negative")

# #4
# a=int(input("Enter a no :"))
# if a%2==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

# #6
# s=input("Enter a char: ")
# if s.alpha():
#     print("It is a alphabet ")
# else:
#     print("Not a alphabet")

# #7
# s=input("Enter a char : ")
# vow="AEIOUaeiou"
# if s in vow:
#     print("The character is a vowel")
# else:
#     print("COnsonant")

# #8
# import string
# a=input("Enter : ")
# if a.isalpha():
#     print("It is a alphabet")
# elif a.isdigit():
#     print("It is a digit ")
# elif a in string.punctuation:
#     print("Special character")
# else:
#     print("Invalid input")

# #9
# a=input("Enter a char : ")
# if a>=65 and a<91:
#     print("Upper Case")
# else:
#     print("Lower Case")

# #10
# a=(input("Enter week no : "))
# match a:
#     case "1" : print("Monday")
#     case "2" : print("Tuesday")
#     case "3" : print("Wednesday")
#     case "4" : print("THursday")
#     case "5" : print("Friday")
#     case "6" : print("Saturday")
#     case "7" : print("sunday")
#     case _   : print("Invalid input")

# #11
# a=input("Enter month no :")
# match a:
#     case "1" : print("January has 31 days")
#     case "2" : print("February has 28/29 days")
#     case "3" : print("March has 31 days")
#     case "4" : print("April has 30 days")
#     case "5" : print("May has 31 days")
#     case "6" : print("June has 30 days")
#     case "7" : print("July has 31 days")
#     case "8" : print("August has 31 days")
#     case "9" : print("September has 30 days")
#     case "10" : print("October has 31 days")
#     case "11" : print("November has 30 days")
#     case "12" : print("December has 31 days")
#     case _    : print("Invalid Input")

#13
# side1=int(input("ENter angle side : "))
# side2=int(input("ENter angle side : "))
# side3=int(input("ENter angle side : "))
# tri=side1+side2+side3
# if tri == 180 :
#     print("Valid triangle")
# else:
#     print("Invalid Traingle ")

#14 Input all sides of a triangle and check whether triangle is equilateral, isosceles or 
# scalene triangle or not.
# side1=int(input("ENter angle side : "))
# side2=int(input("ENter angle side : "))
# side3=int(input("ENter angle side : "))

# match (side1==side2,side2==side3,side3==side1):
#     case (True,False,False)|(False,True,True)|(False,False,True):
#         print("ISocelene")
#     case (True,True,True):
#         print("Equilateral")
#     case _:
#         print("Scalene")


# 15. Find all roots of a quadratic equation
import math

# a = int(input("Enter coefficient of x^2 (a): "))
# b = int(input("Enter coefficient of x (b): "))
# c = int(input("Enter constant term (c): "))

# d = b**2 - 4*a*c

# if d < 0:
#     print("No real roots (complex roots)")
# else:
#     r11 = (-b + math.sqrt(d)) / (2*a)
#     r22 = (-b - math.sqrt(d)) / (2*a)
#     print(f"The roots of the quadratic equation are: {r11}, {r22}")


# 16. Addition of two number without addition operator
# a=int(input("enter no : "))
# b=int(input("enter no : "))
# summ=a^b
# print(summ)


# 17. Program to print how many inputs are given by user
# a=input("Enter inputs : ")
# bs=a.split()
# c={}
# for b in bs:
#     if b in c:
#         c[b]+=1
#     else:
#         c[b]=1

# print(c)
# 23. Program to swap two numbers
# a=int(input("ENTer : "))
# b=int(input("ENTer : "))
# def swap(a,b):
#     temp=a
#     a=b
#     b=temp
#     return f"a is {a}\nb is {b}"
# print(swap(a,b))

# 24. Program to find factorial of a number
# num=int(input("Enter no : "))
def factorial(num):
     fact=1
     for i in range(1,num+1):
          fact*=i
     return fact
# factorial(num)
# 25. Program to calculate the sum of natural numbers
# n=int(input("Enter n : "))
# n_sum=n*(n+1)//2
# print(n_sum)
# 26. Program to generate multiplication table
# n=int(input("Enter no. : "))
# def table(n):
#     for i in range(1,11):
#         print(f"{n}x{i}={n*i}")
# table(n)
# 27. Program to display Fibonacci series
# fic=int(input("Enter no : "))
def fibonacci(num):
    if num==0:
        return 0
    elif num==1 or num==2:
        return 1
    else:
        a,b=0,1
        for i in range(2,num):
           a,b=b,a+b
        return b
# print(fibonacci(fic))

#28
# a=int(input("Enter : "))
# b=int(input("Enter : "))
# def gcd(aa,bb):
#     a=max(aa,bb)
#     b=min(aa,bb)
    
#     while True:
#         r=a%b
#         if r==0:
#             break
#         a=b
#         b=r
        
#     return b
# print(gcd(a,b))

# 29
# a=int(input("Enter : "))
# b=int(input("Enter : "))
# def lcm(aa,bb):
#      a=max(aa,bb)
#      b=min(aa,bb)
#      while True:
#           r=a%b
#           if r==0:
#                break
#           a=b
#           b=r
          
     
#      return aa*bb/b

# print(lcm(a,b))

#30
# for i in range(65,91):
#     print(chr(i))

#31
# num=int(input("Enter number : "))
# poww=int(input("Enter power"))
# power=1
# for i in range(1,poww+1):
#     power=power*num
# print(power)

#32
# num=12345
# rev=0
# while True:
#     if num==0:
#         break
#     number=num%10
#     rev=rev*10+number
#     num=num//10

# print(rev)

#33
# num=2322
# temp=num
# rev=0
# while True:
#     if num==0:
#         break
#     number=num%10
#     rev=rev*10+number
#     num=num//10

# if rev==temp:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#35
# num=int(input("Enter a number : "))
def prime(n):
    if n==1:
        print(f"{n} IS NOT A PRIME NUMBER")
        return
    for i in range(2,n-1):
        if n%i==0:
            print(f"{n} IS NOT A PRIME NUMBER")
            return
     
    print(f"{n} IS A PRIME NUMBER")
            



# prime(num)

#34
# number=int(input("Enter n : "))
# for i in range(1,number+1):
#     prime(i)

#36
# num=int(input("Enter number : "))
def armstrong(n):
    temp=n
    total=0
    while True:
        if n==0:
            break
        num=n%10
        cube=num**3
        total+=cube
        n=n//10
    if temp==total:
        print(f"{temp} : Armstrong")
    else:
        print(f"{temp} : Not an Armstrong")
# armstrong(num)

#37
# number=int(input("Enter range : "))
# for i in range(1,number+1):
#     armstrong(i)

#38
# num=int(input("Enter no :"))
def strongnum(n):
     total=0
     temp=n
     while True:
         if n==0:
             break
         num=n%10
         a=factorial(num)
         total+=a
         n=n//10
     if temp==total:
         print(f"{temp} is a strong number")
     else:
         print(f"{temp} is not a strong number")
         
# strongnum(num)

#39
# a=int(input("Enter strt range : "))
# b=int(input("Enter end range : "))
# for i in range(a,b+1):
#     strongnum(i)

# a=int(input("Enter a number : "))
# armstrong(a)
# prime(a)
# strongnum(a)
#41
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# found = False
# for i in range(2, num // 2 + 1):
#     if is_prime(i) and is_prime(num - i):
#         print(f"{num} = {i} + {num - i}")
#         found = True
# if not found:
#     print("Cannot be expressed as sum of two prime numbers")

#42
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

n = int(input("Enter a number: "))
print("Sum =", sum_natural(n))

#43
num = int(input("Enter a number: "))
print("Factors:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)



#44
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result =", a + b)
elif op == '-':
    print("Result =", a - b)
elif op == '*':
    print("Result =", a * b)
elif op == '/':
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero error!")
else:
    print("Invalid operator")



#45
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


#46
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD =", gcd(a, b))



#47
# Binary to Decimal
binary = input("Enter binary number: ")
decimal = int(binary, 2)
print("Decimal:", decimal)

# Decimal to Binary
decimal = int(input("Enter decimal number: "))
binary = bin(decimal)[2:]
print("Binary:", binary)





#48
# Octal to Decimal
octal = input("Enter octal number: ")
decimal = int(octal, 8)
print("Decimal:", decimal)

# Decimal to Octal
decimal = int(input("Enter decimal number: "))
octal = oct(decimal)[2:]
print("Octal:", octal)




#49
def reverse(sentence):
    if len(sentence) == 0:
        return ""
    return reverse(sentence[1:]) + sentence[0]

s = input("Enter a sentence: ")
print("Reversed:", reverse(s))


#50
# lis=[2,4,56,6,7]
# print(sum(lis)/len(lis))

#51
# lis=[2,4,56,6,7]
# maxx=lis[0]
# for i in lis:
#     if maxx < i:
#         maxx=i
# print(maxx)
    
    
    
    
