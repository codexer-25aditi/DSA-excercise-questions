class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c=len(arr)//4
        for i in arr:
            if arr.count(i)>c:
                return i
        
        