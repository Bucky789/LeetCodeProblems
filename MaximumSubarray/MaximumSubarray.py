from typing import List


def maxSubArray(nums: List[int]) -> int:
    current = maximum = nums[0]

    for num in nums[1:]:
        if current < 0:
            current = num
        else:
            current += num
        if current > maximum:
            maximum = current

    return maximum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))