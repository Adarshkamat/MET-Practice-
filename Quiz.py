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
j=1
for i in questions:
    print(f"Question {j}: {i["question"]}")
    j+=1
    print(f"""Options: 
    {i["option"][0]}
    {i["option"][1]}
    {i["option"][2]}
    {i["option"][3]}""")
                
    a=input("Enter your answer - [a,b,c,d] : ")
    if a==i["answer"]:
        print("Correct Answer : ",a)
        count+=1

print(f"Your score :{count}/3")  





#QUIZ TWO WITH SOME MODIFICATONS
question=[{
    "Question":"What is the capital of Telangana",
    "Option":["A.Hyd","B.Andhra P","C.Khamam"],
    "Answer":"A"
},
{
    "Question":"What is the capital of India",
    "Option":["A.Hyd","B.Mumbai ","C.Delhi"],
    "Answer":"C"
},{
    "Question":"How many continents are there",
    "Option":["A.7","B.5 P","C.3"],
    "Answer":"A"
}]

count=0
history=[]
for i,q in enumerate(question):
    print(f"Question{i+1} : ",q["Question"])
    for j in q["Option"]:
        print(j)
    a=input("Enter the answer : ").upper()
    attempt=(i+1 , a , q["Answer"])
    history.append(attempt)
    if a==q["Answer"]:
       count+=1
    print()
    print()
    
print(f"Your Score for this Quiz is : {count}/{len(question)}")
print("Q_no ur_ans  crct_ans")
for k in history:
    print("",k)






