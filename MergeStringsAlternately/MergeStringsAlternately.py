def mergeAlternately(word1: str, word2: str) -> str:
        strFinal = []
        maxLength = max(len(word1), len(word2))
        for i in range(maxLength):
            if i < len(word1):
                strFinal += word1[i]
            if i < len(word2):
                strFinal += word2[i]

        return "".join(strFinal)

word1 = "Helloa"
word2 = "World"
print(mergeAlternately(word1,word2))