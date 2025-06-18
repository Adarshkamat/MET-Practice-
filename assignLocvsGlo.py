#17-6-25
def q(*b):
     return sum(b)

print(q(1,3,2,4,5))


# def a(**b):
#     return ",".join(b)


# print(a(name="bhavn",age=34))


# while True:
#     a=input("Enter Somethhing:")
#     if a=='exit':
#         break

# i=1
# while True:
#     print(i)
#     i+=1
#     if i==5:
#         break

# while True:
#     a=int(input("Enter a no:"))
#     if a<0:
#         continue
#     else:
#         break

# def maxx(*args):
#     i=0
#     mac=args[i]
#     while i<len(args):
#         if args[i]>mac:
#             mac=args[i]
#         i+=1
#     return mac
# print(maxx(1,3,5,7,9))

# l=[]
# while True:
#     a=input("Enter :")
#     if a == "":
#         break
#     l.append(a)
# for i in range(len(l)):
#     print(l[i])


# def su(**kea):
#      return sum(kea.values())

# a={
#      "product1":9000,
#      "product2":1000,
#      "product4":3000
# }

# print(su(**a))

# j=10
# while 0<j:
#      if j==5:
#           j-=1
#           continue
#      print(j)
#      j-=1

def validAge(age):
     while True:
          a=int(input("enter Age:"))
          if a==age:
               print(a)
               break
          
validAge(32)
     