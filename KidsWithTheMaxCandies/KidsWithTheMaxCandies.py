from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = 0
        for i in candies:
            if(i > maxCandies):
                maxCandies = i
        
        for i in candies:
            if(i + extraCandies >= maxCandies):
                result.append(True)
            else:
                result.append(False)

        return result

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))