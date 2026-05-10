class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]

        maxArea = 0
        # create a stack of (index, height)
        #   where height is monotonically increasing
        #   index is last index that height can extend to
        longestRunningRect = [ (0, heights[0] )]

        for i in range(1, n):
            curr = heights[i]
            # print(longestRunningRect, maxArea)
            # curr height is greater than or equal to previous bar
            lastIndex = i
            while longestRunningRect and longestRunningRect[-1][1] > curr:
                lastIndex, lastHeight = longestRunningRect.pop()
                currArea = (i - lastIndex) * lastHeight
                maxArea = max( maxArea, currArea )
                # print('popping, ', longestRunningRect, maxArea)
            longestRunningRect.append( ( lastIndex, curr ) )
        # print(longestRunningRect, maxArea)
        
        while longestRunningRect:
            lastIndex, lastHeight = longestRunningRect.pop()
            currArea = (n - lastIndex) * lastHeight
            # print(currArea)
            maxArea = max( maxArea, currArea )
        return maxArea
            