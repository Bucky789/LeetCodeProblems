from functools import cmp_to_key
from typing import List


def largestNumber(nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare))

        result = ''.join(nums_str)
        return '0' if result[0] == '0' else result


nums = [3,30,34,5,9]
print(largestNumber(nums))