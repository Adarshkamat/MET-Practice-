#   1. Identify three electronic devices in your home. For each device, list 3 properties (like brand, color,
# etc.) and 2 actions (like turn_on, reset, etc.). Then, create a class for each device with these
# attributes and methods. Create instances and call some methods.
# class tv():
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def turn_on(self):
#         print("Turning on..")
#     def volume(self,volume):
#         print(f"The volume has set to {volume}")
# class refridge():
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def turn_on(self):
#         print("Turning on..")
#     def temp(self,temp):
#         print(f"The temp has set to {temp}")
# class mobile():
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def turn_on(self):
#         print("Turning on..")
#     def volume(self,volume):
#         print(f"The volume has set to {volume}")

# TV=tv("lg","white")
# TV.turn_on()
# TV.volume(67)

# # Think of three types of vehicles (e.g., Car, Bike, Truck). Define relevant properties (like model,
# # speed, fuel_type) and actions (like accelerate, stop, honk). Write classes for each and create
# # objects. Demonstrate usage with print statements in each method.
# class car():
#     def __init__(self,model,speed,fuel):
#         self.model=model
#         self.speed=speed
#         self.fuel=fuel

#     def accelerate(self):
#         print("Accelerated")
#     def stop(self):
#         print("Stop")
#     def honk(self):
#         print("honk honk !")

# class bike():
#     def __init__(self,model,speed,fuel):
#         self.model=model
#         self.speed=speed
#         self.fuel=fuel

#     def accelerate(self):
#         print("revved")
#     def stop(self):
#         print("Stopped")
#     def honk(self):
#         print("pee pee !")

# class truck():
#     def __init__(self,model,speed,fuel):
#         self.model=model
#         self.speed=speed
#         self.fuel=fuel

#     def accelerate(self):
#         print("speedUp")
#     def stop(self):
#         print("Stop ok please")
#     def honk(self):
#         print("ting ting !")

# c=car("SUV",180,"CNG")
# print(c.model)
# print(c.speed)
# c.honk()

# # Imagine a School System with objects like Student, Teacher, and Classroom. Define suitable
# # properties and methods for each. Create classes and instantiate objects for each, and call their
# # methods.
# class classroom:
#     def __init__(self,class_std,room_no):
#         self.class_std=class_std
#         self.room_no=room_no
#     def room(self):
#         print(f"Teacher teaches students in {self.room_no} room ")

# class students:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def study(self):
#         print(f"{self.name} is studying")

# class teacher:
#     def __init__(self,name,subject_teaches):
#         self.name=name
#         self.subject=subject_teaches
#     def teches(self):
#         print(f"{self.name} teaches to the stuents")

# cl=classroom(8,101)
# cl.room()
# st=students("adarsh",14)
# st.study()
# te=teacher("Dr.Shubhash","science")
# te.teches()




# # 4. Consider a Shopping App with objects like Product, Cart, and User. Identify at least 3 attributes
# # and 2 actions for each. Write classes, create objects, and simulate actions like adding products to
# # cart or viewing product details.
# # class shopping_app:
# #     def __init__(self,user):
# #         self.user=user
# #         self.cart=[]
# #     def products(self,product):
# #         a=input("ADD TO CART : ").lower()
# #         if a == "yes":
# #             self.cart.append(product)
# #     def cartii(self):
# #         for i in self.cart:
# #             print(i)
# # shop=shopping_app("Adarsh")
# # shop.products("Chips")
# # shop.products("Soft drink")
# # shop.cartii()

# # 5. Identify objects in a Library like Book, Librarian, and Member. Define attributes (like title, author
# # for Book) and actions (like issue, return, read). Write classes, create instances, and call some
# # method
# class book:
#     def __init__(self,title,book_left,author):
#         self.title=title
#         self.book_left=book_left
#         self.author=author
#     def books(self):
#         print(f"""The Title of the book "{self.title}"
#               The author of the book "{self.author}"
#               books left : {self.book_left}
#             """)
#     def book_stock():
#        print("{ self.book_left}")
# b1=book("AgeofFire",10,"Suresh")
# b1.books()
# class librarian:
#     def __init__(self,library,Book,issue_date):
#         self.library=library
#         self.Book=Book
#         self.issue_date=issue_date
#     def book_issued(self):
#         print(f"The issued book is : {self.book}")
#         self.book_left-=1

# class member:
#     def __init__(self,user_name,user_id):
#         self.user_name=user_name
#         self.user_id=user_id
#     def mem(self):
#         print(f"The member is {self.user_name} with {self.user_id} id")

# user=member("Adarsh","554")
# user.mem()

# 1. Create a class Remote and a class TV. Add a method turn_on() in TV. Inside Remote, create an
# instance of TV and call tv.turn_on() from Remote. Now write similar code for turn_off().
class TV:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print("displaying")
    def blank(self):
        print("Screen out")
class Remote:
    def __init__(self,brands_remote,tv):
        self.remote=brands_remote
        self.tv=tv
    def turnon(self):
        print(f"Turning on {self.tv.brand} TV")
    def turnoff(self):
        print(f"Turning off {self.tv.brand} TV")
tv=TV("LG")
remote=Remote("Lgs",tv)
remote.turnon()

# 2. Model a class Engine and a class Car. Let Car have an instance of Engine. Define a method in
# Engine called start_engine(), and call it using car.engine.start_engine().
class ENGINE:
    def __init__(self,engine_type):
        self.engine_type=engine_type
    def start_engine(self):
        print("staring the engine")
class Car:
    def __init__(self,name,engine):
        self.name=name
        self.engine=engine

Engine=ENGINE("BSIV")
car=Car("XUV",Engine)
car.engine.start_engine()
# 3. Design a class Room and a class Light. Let each Room object contain a Light object. Define a
# method in Light called switch_on(). From a Room instance, call room.light.switch_on().
class room:
    def __init__(self,room_no,light):
        self.room=room_no
        self.light=light
class light:
    def __init__(self):
        pass
    def switch_on(self):
        print("switched on")

LIGHT=light()
Room1=room(101,LIGHT)
Room1.light.switch_on()
# 4. Create a class Laptop and a class Battery. Let Laptop have a Battery instance. Add a method in
# Battery called check_charge(). Call it from Laptop like laptop.battery.check_charge().
class Laptop:
    def __init__(self,name,B):
         self.name=name
         self.B=B
class Battery:
    def __init__(self,Lap_battery):
        self.Lap_bat=Lap_battery
       
    def check_charge(self,charge):
        if charge >=50:
            print("Charged")
        else:
            print("Battery Low")
battery=Battery("DELLS")
LAP=Laptop("dell",battery)

LAP.B.check_charge(58)

# 5. Create classes Mobile and Camera. The Mobile class should have a Camera object. Add a
# take_picture() method to Camera and call it using mobile.camera.take_picture()
class CAmera:
    def __init__(self):
        pass
    def click(self):
        print("Image Clicked")
class Mobile:
    def __init__(self,brand,cam):
        self.brand=brand
        self.cam=cam
Cam=CAmera()
redmi=Mobile("REdmi",Cam)
redmi.cam.click()