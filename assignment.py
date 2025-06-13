#1
# fruits = [["apple","mango"],["orange","pine"],["dragon","grapes"]]
#print(fruits[-1][0])

#2
# tu=((0,3),(9,0),(4,3))
# print(tu[-1][1])

#3
# stu=[("alice",23),("bob",43)]
# print(stu[-1][-1])

#4
# teo=([10,20],[30,40])
# print(teo[-1][-1])

#5
# stu=[{"name":"Adarsh","age":19},
#      {"name":"bhavan","age":19}]
# print(stu[0]["name"])

#6
# sub_marks={
#     "science":[10,40],
#     "maths":[47,84]
# }
# print(sub_marks["science"][1])

#7
dic={
    "alice":{"age":32,"id":554},
     "john":{"age":42,"id":654}
}
print(dic["alice"])

#8
billing = [  {
                  "status":"paid",
                  "orderNo":4343

        }
]
print(billing[0]["status"])


#9

tupel= ( {
          "status":"paid",
         "orderNo":4343,
         "amount":4000},
         {"status":"pending",
         "orderNo":4343,
         "amount":7000}
       )
print(tupel[0]["amount"])

#10
lis=[("delhi","36C"),("mumbai","39C")]
print(lis[-1][-1])

#11
user={
    "alice":[65,75,56],
    "han":[65,57,33],
    "alex":[76,88,77]
}
print(user["alex"][-1])

#12
lis=[{
    "product":"oil",
    "price":5454

},{
    "product":"milk",
    "price":54

}
]
print(lis[-1]["product"])


#13

lis=[("Maths",[65,75,45]),("Science",[76,77,45])]
print(lis[0][-1][1])

#14
weeks={
    "mon":("run","swim")
    ,"tue":("pray","read")
    ,"wed":("library","learn")
    ,"thu":("travel","exercise")
    ,"fri":("eat","jump")
    ,"sat":("movie","eat"),
    "sun":("chill","rest")
}
print(weeks["mon"][0])

#15
students = [
         {
        "name": "Alice",
        "marks": 
        {
            
    "Math": 85,
            "Science": 90,
            "English": 78
        }
    },
    {
        "name": "Bob",
        "marks":
          {
            
    "Math": 92,
            "Science": 88,
            "English": 80
        }
    }
]

print(students[0]["marks"]["Math"])
