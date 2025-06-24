#   1. Identify three electronic devices in your home. For each device, list 3 properties (like brand, color,
# etc.) and 2 actions (like turn_on, reset, etc.). Then, create a class for each device with these
# attributes and methods. Create instances and call some methods.
class tv():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def turn_on(self):
        print("Turning on..")
    def volume(self,volume):
        print(f"The volume has set to {volume}")
class refridge():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def turn_on(self):
        print("Turning on..")
    def temp(self,temp):
        print(f"The temp has set to {temp}")
class mobile():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def turn_on(self):
        print("Turning on..")
    def volume(self,volume):
        print(f"The volume has set to {volume}")

TV=tv("lg","white")
TV.turn_on()
TV.volume(67)

# Think of three types of vehicles (e.g., Car, Bike, Truck). Define relevant properties (like model,
# speed, fuel_type) and actions (like accelerate, stop, honk). Write classes for each and create
# objects. Demonstrate usage with print statements in each method.
class car():
    def __init__(self,model,speed,fuel):
        self.model=model
        self.speed=speed
        self.fuel=fuel

    def accelerate(self):
        print("Accelerated")
    def stop(self):
        print("Stop")
    def honk(self):
        print("honk honk !")

class bike():
    def __init__(self,model,speed,fuel):
        self.model=model
        self.speed=speed
        self.fuel=fuel

    def accelerate(self):
        print("revved")
    def stop(self):
        print("Stopped")
    def honk(self):
        print("pee pee !")

class truck():
    def __init__(self,model,speed,fuel):
        self.model=model
        self.speed=speed
        self.fuel=fuel

    def accelerate(self):
        print("speedUp")
    def stop(self):
        print("Stop ok please")
    def honk(self):
        print("ting ting !")

c=car("SUV",180,"CNG")
print(c.model)
print(c.speed)
c.honk()


    
