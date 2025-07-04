from collections import defaultdict
from typing import List


def majorityElement(nums: List[int]) -> int:
    n = len(nums)
    m = defaultdict(int)
        
    for num in nums:
        m[num] += 1
        
    n = n // 2
    for key, value in m.items():
        if value > n:
            return key
        
    return 0


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))