class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arr=[]
        n=len(nums)
        for i in range (0,n):
            arr.append(nums[nums[i]])
        return arr
            

    
