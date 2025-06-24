def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    maxLength = 0
    chars = {}

    for end,i in enumerate(s):
        chars[i] = 1 + chars.get(i, 0)
        while chars[i] > 1:
            chars[s[start]] -= 1
            start += 1
        
        maxLength = max(maxLength, end - start + 1)

    return maxLength

s = "abcabcbb"
print(lengthOfLongestSubstring(s))