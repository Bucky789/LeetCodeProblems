from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def findLeft():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                index = mid
        return index

    def findRight():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                index = mid
        return index

    return [findLeft(), findRight()]
        
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))