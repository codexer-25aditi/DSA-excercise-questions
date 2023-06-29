class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxx=max(candies)
        li=[False]*len(candies)
        for i in range(0,len(candies)):
            sum=extraCandies+candies[i]
            if sum>=maxx:
                li[i]=True
        
        return li
    