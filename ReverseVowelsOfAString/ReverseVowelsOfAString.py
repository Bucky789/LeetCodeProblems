from typing import List


def reverseVowels(s: str) -> str:
    def isVowel(s: chr) -> bool:
            return s.lower() in 'aeiou'
    start = 0
    end = len(s)-1
    lst = list(s)

    while start < end :
        isstartVowel = isVowel(lst[start])
        isendVowel = isVowel(lst[end])
        if (isstartVowel and isendVowel) :
            lst[start] , lst[end] = lst[end], lst[start]
            start = start + 1
            end = end - 1
        elif isVowel(lst[start]) and not isVowel(lst[end]):
            end = end - 1
        elif not isVowel(lst[start]) and isVowel(lst[end]):
            start = start + 1
        else:
            start = start + 1
            end = end - 1
            
    return "".join(lst)


print(reverseVowels("IceCreAm"))