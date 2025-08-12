from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    
    def backtrack(start, path):
        res.append(path[:])  # store current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # undo choice
    
    backtrack(0, [])
    return res

nums = [1,2,3]
print(subsets(nums))