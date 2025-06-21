from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)
    if (target > nums[end - 1]):
        return end
    while (start <= end):
        mid = (start + end) // 2
        if (nums[mid] == target):
            return mid
        if (target < nums[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return start

nums = [1,3,5,6]
target = 7
print(searchInsert(nums,target))