def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    count = 0 
    maxCount = 0

    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        if i >= k and s[i - k] in vowels:
            count -= 1
        maxCount = max(maxCount, count)

    return maxCount

s = "abciiidef"
k = 3
print(maxVowels(s,k))