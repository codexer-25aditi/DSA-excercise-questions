#Neon number
#Square the number and add the digits when equal to input it is a neon number

def checkNeon(num):
    a=num
    num=num*num
    sum=0
    while num!=0:
        r=num%10
        sum=sum+r
        num=num//10
    
    if sum==a:
        return True
    else:
        return False
    



num=int(input())
print(checkNeon(num))
