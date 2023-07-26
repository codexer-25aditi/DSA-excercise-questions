
def solve(s):
    sum=0
    for i in range(len(s)):
        sum=sum+ord(s[i])
    return (format((sum/len(s)),"0.2f"))
        


s=input()
print(solve(s))
