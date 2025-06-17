#16-6-25
# def greet(name):
#     return f"Hello {name}"

# print(greet("Bhavan"))



# def fever(temp):
#     ill=False
#     if temp >99:
#         ill=True
    
#     return ill

# print("Am i ill?",fever(101))


# def get_last_fruit(listt):
#     return listt[-1]

# a=["apple","banana","orange","mango"]
# print(get_last_fruit(a))

# def get_price_tag(price):
#     if price>1000:
#         return f"{price} is expensive"
#     else:
#         return f"Affordable"

# print(get_price_tag(15000))

# def format_user_info(name,age):
#     return f"{name} is {age}"

# print(format_user_info(name="Adarsh",age=43))


# def to_upper(stri):
#     if type(stri)==str:
#         return stri.upper()
#     else:
#         return "invalid input"
    
# print(to_upper("adarsh"))

# . Write a function 'safe_divide' that takes two numbers as keyword arguments 'num' and 'den'.
# Return the result if den is not 0, else return 'Cannot divide'

# def safe_divide(num,den):
#     if den==0:
#         return "Cannot Divide"
#     else:
#         return num/den
    
# print(safe_divide(5,0))

# Write a function 'check_login' that takes a dictionary with 'username' and 'password'. Return
# 'Login successful' if password is not empty.
# def check_login(dic):
#     if dic["password"]!="":
#         return "login succesfull"
#     else :
#         return "Login unsuccsful"
    
# a={"username":"Adaarsh","password":"4343saa"}
# print(check_login(a))

# . Create a function 'get_full_name' that takes 'first' and 'last' as named arguments and returns full
# name in title case.
# def full_name(first,last):
#    fullName=first + last
#    return fullName.title()

# print(full_name("adarsh","Kamat"))

# rite a function 'get_discounted_price' that takes 'price' and 'is_member'. If is_member is True,
# return price * 0.9 else return price.
def get_discount(price,isMember):
    if isMember:
        return f" {price * 0.9}"
    else:
        return price
    
print(get_discount(1000,True))