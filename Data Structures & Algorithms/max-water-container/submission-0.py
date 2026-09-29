class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        mx = 0
        while l < r:
            x = min( heights[l], heights[r] )
            mx = max( mx, x * (r - l) )
            if heights[l] > heights[r]:
                r = r - 1 
            else:
                l = l + 1
        
        return mx