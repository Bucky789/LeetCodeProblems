from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closestSum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            
            if abs(currSum - target) < abs(closestSum - target):
                closestSum = currSum
            
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else: 
                return currSum

    return closestSum

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums,target))