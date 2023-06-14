#check the sum of 2 elements in array is equal to target and print them
#[2,7,1,3] and target =9

def checkSum(arr,target):

    sum=0

    for i in range(0,len(arr)-1):
        sum=sum+arr[i]
        for a in range(1,len(arr)-1):
            sum=arr[i]+arr[i+a]
            if sum==target:
                return [arr[i],arr[i+a]]
    return 0



arr=[2,7,1,3]
target=9
print(checkSum(arr,target))
