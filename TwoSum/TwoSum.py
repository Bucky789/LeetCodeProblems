from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
        match = []
        remainders = {}
        for i in range(len(nums)):
            if (target - nums[i]) in remainders:
                match.append(remainders[target - nums[i]])
                match.append(i)
            else:
                remainders[nums[i]] = i
        return match
    

nums = [3,4,5,6]
target = 7
print(twoSum(nums,target))