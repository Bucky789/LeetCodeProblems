from typing import List


def largestAltitude(gain: List[int]) -> int:
        maxAltitude = 0
        altitudes = [0]
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])
            if(altitudes[-1] > maxAltitude):
                maxAltitude = altitudes[-1]
        return maxAltitude


gain = [-5,1,5,0,-7]
print(largestAltitude(gain))