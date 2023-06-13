
def Kapreckers(num):
    num=num*num
    num=str(num)
    length=len(num)
    for i in range(1,length):
        left="".join(num[:i])
        right="".join(num[i:])
        if left+right==num:
            return 1
    return 0

n=int(input())
a=Kapreckers(n)
if a==1:
    print("True")
else:
    print("False")














