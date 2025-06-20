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