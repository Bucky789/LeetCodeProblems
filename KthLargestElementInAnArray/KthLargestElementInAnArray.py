import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    minHeap = []

    for num in nums:
        heapq.heappush(minHeap, num)
        if len(minHeap) > k:
            heapq.heappop(minHeap)

    return minHeap[0]


nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))