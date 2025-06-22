def palindrome(string):
    l=len(string)
 
    for i in range(l):
        if string[i]==string[l-i-1]:
            pass
        else:
            return False
    return True

def fact(num):
    f=1
    for i in range(num+1):
        if i!=0:
            f*=i
    return f

def prime(num):
    if num < 2:
        return False
    for i in range(2,num-1):
        if num%i==0:
            return False
    return True

def sec_max(lis):
    maxx=max(lis)
    print(maxx)
    lenn=len(lis)
    sec_m=min(lis)
    for i in range(lenn):
        if lis[i]!=maxx and lis[i]>sec_m:
            sec_m=lis[i]
    print(sec_m)


sec_max([9,8,3,4,2])
for i in range(1,111):
    if prime(i):
        print(f"{i}prime")
    else:
        print(f"{i}Not a prime")
# print(palindrome("cattac"))
# print(prime(9))
# print(fact(7))

