#1
a,b=5,7
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

#2
a,b,c=5,4,22
if a > b and a > c :
    print(f"{a} is greater")
elif b > c and b > a :
    print(f"{b} is greater")
else:
    print(f"{c} is greater")

#3
a=int(input("Enter a no :"))
if a>0:
    print(f"{a} is positive")
elif a==0:
    print("It is Zero")
else:
    print(f"{a} is negative")

#4
a=int(input("Enter a no :"))
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

#6
s=input("Enter a char: ")
if s.alpha():
    print("It is a alphabet ")
else:
    print("Not a alphabet")

#7
s=input("Enter a char : ")
vow="AEIOUaeiou"
if s in vow:
    print("The character is a vowel")
else:
    print("COnsonant")

#8
import string
a=input("Enter : ")
if a.isalpha():
    print("It is a alphabet")
elif a.isdigit():
    print("It is a digit ")
elif a in string.punctuation:
    print("Special character")
else:
    print("Invalid input")

#9
a=input("Enter a char : ")
if a>=65 and a<91:
    print("Upper Case")
else:
    print("Lower Case")

#10
a=(input("Enter week no : "))
match a:
    case "1" : print("Monday")
                break
    case "2" : print("Tuesday")
                break
    case "3" : print("Wednesday")
                break
    case "4" : print("Thursday")
                break
    case "5" : print("Friday")
                break
    case "6" : print("Saturday")
                break
    case "7" : print("sunday")
                break
    case _   : print("Invalid input")
                break

#11
a=input("Enter month no :")
match a:
    case "1" : print("January has 31 days")
                break
    case "2" : print("February has 28/29 days")
                break
    case "3" : print("March has 31 days")
                break
    case "4" : print("April has 30 days")
                break
    case "5" : print("May has 31 days")
                break
    case "6" : print("June has 30 days")
                break
    case "7" : print("July has 31 days")
                break
    case "8" : print("August has 31 days")
                break
    case "9" : print("September has 30 days")
                break
    case "10" : print("October has 31 days")
                break
    case "11" : print("November has 30 days")
                break
    case "12" : print("December has 31 days")
                break
    case _    : print("Invalid Input")
                break

