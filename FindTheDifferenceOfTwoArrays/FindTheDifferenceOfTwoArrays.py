from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    nums1=set(nums1)
    nums2=set(nums2)
    s1=list(nums1-nums2)
    s2=list(nums2-nums1)
    return [s1,s2]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1,nums2))