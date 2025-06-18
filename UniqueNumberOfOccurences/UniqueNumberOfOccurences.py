from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
        occurences = {}
        for i in arr:
            if(i in occurences):
                occurences[i] += 1
            else:
                occurences[i] = 1
        result = []
        for i in occurences:
            if(occurences[i] in result):
                return False
            else:
                result.append(occurences[i])
        return True
            

arr = [1,2]
print(uniqueOccurrences(arr))