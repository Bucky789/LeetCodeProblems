def isValid(s: str) -> bool:
    stack = []
    parenthesisDict = {")":"(", "}":"{", "]":"["}
    for char in s:
        if char in parenthesisDict.values():
            stack.append(char)
        elif char in parenthesisDict.keys():
            if not stack or parenthesisDict[char] != stack.pop():
                return False
    
    return not stack


s = "()[]{}"
print(isValid(s))