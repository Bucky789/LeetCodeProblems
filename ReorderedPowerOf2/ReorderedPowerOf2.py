from collections import Counter

def reorderedPowerOf2(n: int) -> bool:
    
    def countDigits(x):
        return Counter(str(x))
    
    target = countDigits(n)
    
    for i in range(31):
        if target == countDigits(1 << i):
            return True
    return False

n = 1
print(reorderedPowerOf2(n))