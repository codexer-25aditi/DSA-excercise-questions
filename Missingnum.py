#Find the missing number in given array
#[4,3,2,1,6]

def FindmissingNum(arr):
    mini=min(arr)
    maxi=max(arr)

    li=list()

    for i in range(mini,maxi):
        li.append(i)

    for j in range(0,len(li)):
        if li[j] not in arr:
            return li[j]
    return None


#arr=[4,3,2,1,6]
arr=list(map(int,input().split()))
print(FindmissingNum(arr))




