from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    start = 0
    end = len(nums)-1
    count = 0
    while start < end:
        sumOfNums = nums[start] + nums[end]
        if (sumOfNums == k):
            count += 1
            start += 1
            end -= 1
        elif sumOfNums > k:
            end -= 1
        else:
            start += 1
    return count


nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
print(maxOperations(nums,k))