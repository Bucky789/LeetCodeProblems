def countVowelStrings(n: int) -> int:
    dp = [1] * 5  
    for _ in range(1, n):
        for j in range(3, -1, -1):
            dp[j] += dp[j + 1]  
    return sum(dp)


n = 1
print(countVowelStrings(n))