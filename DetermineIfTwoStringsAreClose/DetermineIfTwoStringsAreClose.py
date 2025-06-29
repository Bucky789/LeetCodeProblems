from typing import Counter


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    if set(word1) != set(word2):
        return False
    
    freq1 = Counter(word1)
    freq2 = Counter(word2)

    return sorted(freq1.values()) == sorted(freq2.values())



word1 = "cabbba"
word2 = "abbccc"
print(closeStrings(word1,word2))