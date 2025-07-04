from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    lcp = strs[0]

    for i in range(1, len(strs)):
        commonPrefix = ""
        for j in range(min(len(lcp), len(strs[i]))):
            if lcp[j] == strs[i][j]:
                commonPrefix += lcp[j]
            else:
                break
        lcp = commonPrefix
        if not lcp:
            return ""

    return lcp


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))