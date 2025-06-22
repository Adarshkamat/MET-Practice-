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

def prime_nos(start,end):
 for i in range(start,end):
    if prime(i):
        print(f"{i}prime")
    else:
        print(f"{i}Not a prime")

 #Stock BUT AND SELL       
prices=[7,1,5,3,6,4]
profit=0
bestBuy=prices[0]
for i in range(len(prices)):
    if(bestBuy<prices[i]):
        profit=max(profit,prices[i]-bestBuy)
    bestBuy=min(prices[i],bestBuy)

def power(x,n):
    binaryForm=n
    ans=1
    while binaryForm>0 :
        if binaryForm%2==1:
            ans*=x
        binaryForm//=2
        x*=x
    return ans 





# print(palindrome("cattac"))
# print(fact(7))
# print(prime(9))
# sec_max([9,8,3,4,2])
# prime_nos(1,111)
# print(profit)
#  print(power())





