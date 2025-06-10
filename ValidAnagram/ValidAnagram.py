def isAnagram(s: str, t: str) -> bool:
        sA = {}
        sB = {}
        check = False
        sizeA = len(s)
        sizeB = len(t)
        for i in s:
            if(i in sA):
                sA[i] += 1
            else:
                sA[i] = 1

    
        for j in t:
            if(j in sB):
                sB[j] += 1
            else:
                sB[j] = 1
        
        if(sizeA < sizeB):
            for k in sB:
                if(k in sA):
                    if(sA[k] == sB[k]):
                        check = True
                    else:
                        return False
                else:
                    return False
        else:
            for k in sA:
                if(k in sB):
                    if(sA[k] == sB[k]):
                        check = True
                    else:
                        return False
                else:
                    return False
        return check


s = "racecar"
t = "carrace"
print(isAnagram(s,t))