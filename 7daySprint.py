# 7-7-2025 in kaggle
# 8-7-2025
# s="abc12def34gh5"
# summ=0
# for char in s :
#     if char.isdigit():
#         summ+=int(char) 
# print(summ) 





# s="abc12def34gh5"
# temp=""
# summ=0
# for char in s :
#     if char.isdigit():
#         temp+=char
#     else:
#         if temp !="":
#             summ+=int(temp)
#             temp=""
# if temp:
#     summ += int(temp)  
# print(summ) 


# a="apple"
# b="plead"
# c=set(a)
# d=set(b)
# common=c&d
# print(common)


# a,b,c=10,25,15

# if a>b:
#     if a>c:
#         print(f"{a} is greater ")
# elif b>a:
#     if b>c:
#         print(f"{b } is greater ")
# else:
#     print(f"{c} is greater ")



# s="swiss"
# for ch in s :
#     if s.count(ch)==1:
#         print(ch)
#         break


import string
# 1. Remove all non-alphabet characters from 'H3ll0_Wor!ld#2025'.
# Expected Output: 'HllWorld'
t='H3ll0_Wor!ld#2025'
c=""
for ch in t:
    if ch.isdigit() :
        pass
    else:
        if ch not in string.punctuation:
         c+=ch
# print(c)

# 2. Find the most frequent word in the sentence: 'cat dog dog bird cat cat'.
# Expected Output: 'cat'
sen='cat dog dog bird cat cat'
animals=sen.split(" ")
c={}
for animal in animals:
   if animal in c:
      c[animal]+=1
   else:
      c[animal]=1
   
   d=max(c.values())
for i in c:
   if c[i]==d:
      print(i)


# 3. Return the index of the first vowel in the string 'crypt'.
# Expected Output: -1 (no vowels found)
s="crypt"
def stringVow(st):
   vowel="aeiou"
   st=st.lower()
   for i in st :
      if i in vowel:
         return 1
   return -1    

# print(stringVow(s))
# 4. Move all vowels in 'education' to the end while preserving order.
# Expected Output: 'dctneuaio'
sen="education"
def vow_at_end(s):
   vowel="aeiouAEIOU"
   vow=[]
   consonant=[]
   for i in s:
      if i in vowel:
         vow.append(i)
      else:
          consonant.append(i)
   s="".join(consonant+vow)
   return s
print(vow_at_end(sen))
         
         
# 5. Create a dictionary mapping each character in 'banana' to its frequency.
# Expected Output: {'b':1, 'a':3, 'n':2}
ban="banana"
dic={}
for i in ban:
   if i in dic:
     dic[i]+=1
   else:
      dic[i]=1
print(dic)
   

# 6. Replace every vowel in 'hello world' with its uppercase form.
# Expected Output: 'hEllO wOrld'
sen = 'hello world'
vow = "AEIOUaeiou"

for s in sen:
    if s in vow:
        a = s.upper()
        sen = sen.replace(s, a)
print(sen)


# 7. Check if digits in '12345' form a continuous ascending sequence.
# Expected Output: True
digit="12345"
def check_digit(f):
    n=len(f)
    for i in range(1,n+1):
        if int(f[i-1])==i:
            pass
        else:
            return "False"
    return "True"

# print(check_digit(digit))
# 8. Count how many words in 'This is a beautiful sunny day' are longer than 4 letters.
# Expected Output: 2
c='This is a beautiful sunny day' 
lis=c.split(" ")
count=0
for a in lis:
   n=len(a)
   if len(a)>4:
      count+=1

# print(count)


# 9. Mask all but last 4 characters of 'mysecretpassword1234' with '*'.
# Expected Output: '****************1234'
c= 'mysecretpassword1234'
n=len(c)-4
d="*"*n+c[-4:]
print(d)

# 10. Convert 'python' to a staircase pattern with one letter per line.
# Expected Output:
# 'p\n y\n t\n h\n o\n n'
a="python"
for j in a:
   print(j)
# 11. Reverse the words in the string 'open ai builds tools'.
# Expected Output: 'tools builds ai open'
d='open ai builds tools'
f=d.split(" ")
e=f[::-1]
print(" ".join(e))
# 12. From 'a1b2c3', extract characters at even indices.
# Expected Output: 'abc
sen='a1b2c3'
rs=""
for i in range(0,len(sen),2):
   if not sen[i].isdigit():
      rs+=sen[i]

print(rs)