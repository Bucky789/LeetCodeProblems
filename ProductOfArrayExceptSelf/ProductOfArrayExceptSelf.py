from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n

    curr = 1
    for i in range(n):
        ans[i] *= curr
        curr *= nums[i]

    curr = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= curr
        curr *= nums[i]

    return ans

nums = [1,2,3,4]
print(productExceptSelf(nums))