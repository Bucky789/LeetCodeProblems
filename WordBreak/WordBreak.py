from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for word in wordSet:
            if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
                break

    return dp[len(s)]


s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s,wordDict))