from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        flowers = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    flowers += 1
        
        return flowers >= n

flowerbed = [1,0,0,0,1]
n = 1

print(canPlaceFlowers(flowerbed,n))