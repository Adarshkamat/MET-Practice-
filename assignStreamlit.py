# import streamlit as s
# import requests 
# s.title("Come Have Fun")
# word = s.text_input("Enter a word : ")
# btn = s.button(" Click To Generate")
# if btn:
#     url = "https://api.datamuse.com/words?ml={word}"
#     response = requests.get(url)
#     data = response.json()
#     if response.status_code==200:
#         for item in data :
#             s.write(item.get("word"))
#     else :
#         s.write("There has been error")

# class member:
#     def __init__(self,name,m_id):
#         self.name=name
#         self.Id=m_id
# class book:
#     def __init__(self,title,author,copies):
#         self.title=title
#         self.author=author
#         self.copies=copies 
#     def issue(self):
#         if self.copies > 0:
#             self.copies-=1
#             print(f"{self.title} issued ")
#         else:
#             print(f"No copies left of {self.title} book")

#     def return_book(self):
#         self.copies+=1
# class librarian:
#     def __init__(self,name):
#         self.name=name
#     def add_book(self,library,book):
#         library.books.append(book)
#         print(f"Added")
#     def remove_book(self,library,book):
#         for books in library.books:
#             if books.title==book.title:
#                 library.books.remove(books)
#                 print(f"{books.title} is removed ")
#                 break
# class library:
#     def __init__(self,name):
#         self.name=name
#         self.books=[]
#         self.members=[]
#     def add_member(self,member):
#         self.members.append(member)
#         print(f"{member.name} is added ")
#     def find_book(self,title):
#         for books in self.books:
#             if books.title==title:
#                 return True
#         return False
#     def issue_book(self,book):
#         if self.find_book(book.title):
#             book.issue()
#     def return_books(self,book):
#         if self.find_book(self,book.title):
#             book.return_book()
#     def display_books(self):
#         print("------------------------")
#         print("AVAILABLE BOOLS")
#         for book in self.books:
#             print(f"-{book.title}")
#         print("------------------------")
#     def display_members(self):
#         print("------------------------")
#         print("AVAILABLE MEMBERS")
#         for mem in self.members:
#             print(mem.name)
#         print("------------------------")


# l1=library("Bhagat Singh Library")
# m1=member("Adarsh",554)
# b1=book("Bhagvad Gita","Tulsidas",5)
# b2=book("Python 101","George wesley",10)
# libn=librarian("Mr.Suresh")
# libn.add_book(l1,b1)
# libn.add_book(l1,b2)
# l1.add_member(m1)
# l1.issue_book(b1)
# l1.issue_book(b1)
# l1.issue_book(b1)
# l1.issue_book(b1)
# l1.issue_book(b1)
# l1.issue_book(b1)
# l1.issue_book(b2)
# print(l1.find_book(b1))
# l1.display_books()
# l1.display_members()


# class Customer:
#     def __init__(self, name, c_id):
#         self.name = name
#         self.id = c_id
#         self.cart = None


# class Product:
#     def __init__(self, product, price, qty):
#         self.p_name = product
#         self.price = price
#         self.qty = qty

#     def is_available(self, qty):
#         return self.qty >= qty


# class Cart:
#     def __init__(self):
#         # trolley = list of dictionaries: {product: Product obj, qty: int}
#         self.trolley = []

#     def add_product(self, product, quantity):
#         if product.is_available(quantity):
#             product.qty -= quantity
#             # Check if product already exists in trolley, update qty
#             for item in self.trolley:
#                 if item["product"].p_name == product.p_name:
#                     item["qty"] += quantity
#                     print(f"{product.p_name} quantity updated in the cart")
#                     return
#             # Else, add new entry
#             self.trolley.append({"product": product, "qty": quantity})
#             print(f"{product.p_name} added to the cart")
#         else:
#             print(f"{quantity} quantity of {product.p_name} not available")

#     def remove_product(self, product, qty=0):
#         for item in self.trolley:
#             if item["product"].p_name == product.p_name:
#                 if qty == 0 or item["qty"] <= qty:
#                     self.trolley.remove(item)
#                     print(f"{product.p_name} removed from the cart")
#                 else:
#                     item["qty"] -= qty
#                     product.qty += qty  # Return to stock
#                     print(f"{qty} of {product.p_name} removed from the cart")
#                 return
#         print(f"{product.p_name} not found in cart")

#     def display_cart(self):
#         if not self.trolley:
#             print("Cart is empty")
#             return

#         print("Cart Contents:")
#         total = 0
#         for item in self.trolley:
#             prod = item["product"]
#             qty = item["qty"]
#             print(f"- {prod.p_name} x{qty} @ ₹{prod.price} each")
#             total += qty * prod.price
#         print(f"Estimated Bill: ₹{total}")


# # Test Run
# c1 = Customer("Adarsh", 554)
# p1 = Product("Lays", 20, 5)
# p2 = Product("Snickers", 40, 10)
# p3 = Product("Dove", 35, 20)

# ct1 = Cart()
# c1.cart = ct1

# c1.cart.add_product(p1, 4)
# c1.cart.add_product(p2, 5)
# c1.cart.add_product(p3, 2)

# c1.cart.display_cart()

# c1.cart.remove_product(p1, 2)
# c1.cart.display_cart()

# class TV:
#     def __init__(self):
#         self.state = "Off"

#     def turn_on(self):
#         if self.state == "On":
#             print("TV is already On.")
#         else:
#             self.state = "On"
#             print("TV is now On.")

#     def turn_off(self):
#         if self.state == "Off":
#             print("TV is already Off.")
#         else:
#             self.state = "Off"
#             print("TV is now Off.")


# class Remote:
#     def __init__(self,tv):
#         self.tv = tv  # Remote has an instance of TV

#     def press_power_on(self):
#         self.tv.turn_on()

#     def press_power_off(self):
#         self.tv.turn_off()


# tv=TV()
# remote1 = Remote(tv)
# remote1.press_power_on()   # Turns TV on
# remote1.press_power_off()  # Turns TV off
# remote1.press_power_off()  # Tries turning off again

# cla

class node:
    def __init__(self,node):
        self.data=node
        self.next=None
# n1=node(7)
# print(n1.data)
# print(n1.next)
class linkedlist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print()
        else:
            a=self.head
            while a is not None:
                print(a.data,end="->")
                a=a.next
n1=node(7)
ll=linkedlist()
ll.head=n1
n2=node(6)
n1.next=n2
n3=node(6)
n2.next=n3
ll.traversal()
