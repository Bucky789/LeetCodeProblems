from typing import List


def compress(chars: List[str]) -> int:
        n = len(chars)
        count = 0
        k = 0
        i = 0

        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                count += 1
                j += 1
            
            chars[k] = chars[i]
            k += 1
            
            if count > 1:
                for ch in str(count):
                    chars[k] = ch
                    k += 1
            
            count = 0
            i = j

        return k

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))