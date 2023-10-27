class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0] * n  
        r = [0] * n
        ans = 0
        lm, rm = 0, 0

        for i in range(n):
            l[i] = lm
            if lm < height[i]:
                lm = height[i]
        for i in range(n - 1, -1, -1):
            r[i] = rm
            if rm < height[i]:
                rm = height[i]
        for i in range(n):
            trapped = min(l[i], r[i]) - height[i]
            if trapped > 0:
                ans += trapped

        return ans
