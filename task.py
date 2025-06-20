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

# menu = {
#     "Dosa":40,
#     "Idli":30,
#     "poori":45,
#     "vada":50,
#     "upma":30
# }

# dish_1choice = input("What do you wnat for ur break fast: ")
# dish_1quantity=int(input("enter Quantity:"))
# dish_2choice = input("What do you wnat for ur break fast: ")
# dish_2quantity=int(input("enter Quantity:"))

# print("Your bill")
# bill = (menu.get(dish_1choice,"enter another dish")*dish_1quantity)+(menu.get(dish_2choice,"enter another dish")*dish_2quantity)
# print(bill)


#Build a simple script  to manage tasks using dictionary.
 
#Ask user to enter task 1 name
#Ask user to enter task 2 name
#Ask user to enter task 3 name
#Ask user to update task 2
#Ask user to delete task 3
#print final tasks

# a=input("Enter task 1:")
# bo=input("Enter task 2:")
# c=input("Enter task 3:")

# task={}
# task.update({"task1":a,"task2":bo,"task3":c})

# print(task)


# d=input("Update task2:")
# task.update({"task2":d})
# print(task)



# e=bool(input("Delete task 3[True or False]:"))
# if e==True:
#     task.pop("task3")
#     print(task)
# else:
#     print(task)


questions=[{
    "question":"India's Capital",
    "option":["A.Delhi","b.Mumbai","c.Hyd","d.Banglore"],
    "answer":"a"
},{
    "question":"Largest Continent",
    "option":["A.Africa","b.Asia","c.sAmerica","d.Australia"],
    "answer":"b"
},{
    "question":"color of mango ",
    "option":["A.red","b.blue","c.green","d.yellow"],
    "answer":"d"
}]

count=0
for i in questions:
    print("Question: ",i["question"])
    print("Options: ",i["option"])
    a=input("Enter your answer - [a,b,c,d] : ")
    if a==i["answer"]:
        count+=1

print(f"Your score :{count}/3")


