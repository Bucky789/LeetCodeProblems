def RomanToInteger(s: str) -> int:
    result = 0
    previous = 0
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(s) - 1, -1, -1):
        current = roman_map[s[i]]
        if current < previous:
            result -= current
        else:
            result += current
        previous = current

    return result


s = "XIV"
print(RomanToInteger(s))