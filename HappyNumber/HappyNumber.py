def isHappy(n: int) -> bool:
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = get_sum_of_squares(n)

    return True

n = 19
print(isHappy(n))