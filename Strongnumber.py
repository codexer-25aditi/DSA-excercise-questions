#sum of the factorial of digits of given input is always same as the input,called as strong number
#145=1!+4!+5!=145

def checkStrong(n):
    sum=0
    num=n
    while(n!=0):
        r=n%10
        fact=1
        for i in range(1,r+1):
            fact=fact*i

        sum=sum+fact

        n=n//10

    if sum==num:
        print("Strong")
    else:
        print("Not Strong")





n=int(input())
checkStrong(n)