
def solve(s):
    a="abcdefghijklmnopqrstuvwxyz"
    s=s.lower()
    for i in range (0,len(a)):
        if a[i] not in s:
            return a[i]
        
s=input()
print(solve(s))
