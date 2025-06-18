from typing import List


def uniqueOccurrences(self, arr: List[int]) -> bool:
    occurrences = {}
    for i in arr:
        occurrences[i] = occurrences.get(i, 0) + 1
    
    seen = set()
    for freq in occurrences.values():
        if freq in seen:
            return False
        seen.add(freq)
    
    return True
            

arr = [1,2]
print(uniqueOccurrences(arr))
