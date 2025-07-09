def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    
    m = len(num1)
    n = len(num2)
    res = [0] * (m + n)

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            mul = int(num1[i]) * int(num2[j])
            p1 = i + j
            p2 = i + j + 1
            total = mul + res[p2]
            
            res[p2] = total % 10
            res[p1] += total // 10

    result = ''.join(map(str, res)).lstrip('0')
    return result

num1 = "123"
num2 = "456"
print(multiply(num1,num2))