import re


def isPalindrome(s: str) -> bool:
        sCleaned = re.sub(r'[^A-Za-z0-9]', '', s)
        if(len(sCleaned) <= 1):
            return True
        else:
            
            start = 0
            end = len(sCleaned) - 1
            result = False
            while end >= start:
                if(sCleaned[start].lower() == sCleaned[end].lower()):
                    result = True
                else:
                    result = False
                    break  
                start += 1
                end -= 1
            return result
        
s = "Was it a car or a cat I saw?"
print(isPalindrome(s))
