class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        h = 0
        w = len(height)-1
        area =  h * w
        max_area = area
        while l<r:
            if height[l]<height[r]:
                h = min(height[l], height[r])
                #w = len(height) - 1

                area = h * w
                max_area = max(max_area, area)
                l+=1
                w-=1

            elif height[l]>height[r]:
                h = min(height[l], height[r])

                area = h * w
                max_area = max(max_area, area)
                r-=1
                w-=1

            elif height[l]==height[r]:
                h = min(height[l], height[r])

                area = h * w
                max_area = max(max_area, area)
                r -= 1
                w -= 1

        return(max_area)

                