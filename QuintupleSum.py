a=list(map(int,input("enter no.s").split()))
b=sum(a)
print(b)

found = False

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        k=b-(a[i]+a[j])
        if k==100:
           print("indices to remove : ",i,",",j)
           first,second=max(i,j),min(i,j)
           a.pop(first)
           a.pop(second)
           found=True
           break
        if found:
            break

print(a)
print(sum(a))


