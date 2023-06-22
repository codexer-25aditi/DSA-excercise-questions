class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        arr=2*n*[None]
        for i in range(0,n):
            arr[i]=nums[i]
            arr[i+n]=nums[i]
        return arr
