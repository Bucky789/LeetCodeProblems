from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    if not nums or len(nums) < 3:
        return False

    a = float('inf')
    b = float('inf')

    for num in nums:
        if num <= a:
            a = num
        elif num <= b:
            b = num
        else:
            return True

    return False

nums = [2,1,5,0,4,6]
print(increasingTriplet(nums))