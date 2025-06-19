from typing import List


def maxArea(height: List[int]) -> int:
    start = 0
    end = len(height) - 1
    maxArea = 0
    while start < end:
        if(maxArea < ((end - start) * (min(height[start],height[end])))):
            maxArea = (end - start) * (min(height[start],height[end]))
            if(height[start] <= height[end]):
                start += 1
            else:
                end -= 1
        else:
            if(height[start] <= height[end]):
                start += 1
            else:
                end -= 1
    return maxArea


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))