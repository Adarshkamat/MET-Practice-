students = [
    {"name": "Alice", "marks": [80, 85, 90]},
    {"name": "Bob", "marks": [70, 75, 68]},
    {"name": "Charlie", "marks": [90, 92, 88]}
 ]
# # Task:
# # Write a function that calculates average marks for each student,
# # then sorts and prints
# for i in range(0,len(students)):
#     a=(students[i]["marks"])
#     b=sum(a)
#     print(b)



# 1 What you want?
    #total bill
# 2 What do u need to achieve 
    #dishes and prices 
    #what user wants 
    #how many the user want 
# 3 Arrange the order 
    #dishes and prices 
    #what user wants 
    #how many the user want
# 4 Write the code

menu = {
    "Dosa":40,
    "Idli":30,
    "poori":45,
    "vada":50,
    "upma":30
}

dish_1choice = input("What do you wnat for ur break fast: ")
dish_1quantity=int(input("enter Quantity:"))
dish_2choice = input("What do you wnat for ur break fast: ")
dish_2quantity=int(input("enter Quantity:"))

print("Your bill")
bill = (menu.get(dish_1choice,"enter another dish")*dish_1quantity)+(menu.get(dish_2choice,"enter another dish")*dish_2quantity)
print(bill)





