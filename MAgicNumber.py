n=input()
sum=0
for i in range(len(n)):
    sum=sum+int(n[i])

while sum>9:
    S=0
    while(sum!=0):
        r=sum%10
        S=S+r
        sum=sum//10
    sum=S


if sum==1:
    print("Magic number")
else:
    print("Not a Magic number")










