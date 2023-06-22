class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result=[0]*(2*n)
        for i in range(n):
            result[2*i]=nums[i]
            result[2*i+1]=nums[n+i]
        return result