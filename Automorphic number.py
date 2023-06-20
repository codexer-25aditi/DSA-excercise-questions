#take input as integer ,square the number ,if the last digit is equal to the input,it is called as automorphic number
def checkAutomorphic(num):
    square=num*num

    digits=len(str(num))
    r = square % pow(10,digits)

    if r==num:
        print("Automorphic number")
    else:
        print("Not")


num=int(input())
checkAutomorphic(num)