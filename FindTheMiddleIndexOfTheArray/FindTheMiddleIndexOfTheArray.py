from typing import List


def findMiddleIndex(nums: List[int]) -> int:
    total = 0
    leftSum = 0
    for i in nums:
          total += i
    
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if (leftSum == rightSum):
            return i
        leftSum += nums[i]

    return -1


nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))

