from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    usedNums = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if usedNums[i]:
                continue
            
            if i > 0 and nums[i] == nums[i - 1] and not usedNums[i - 1]:
                continue

            usedNums[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            usedNums[i] = False

    backtrack([])
    return res

nums = [1,1,2]
print(permuteUnique(nums))