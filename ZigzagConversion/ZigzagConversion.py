def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    currRow = 0
    goingDown = False

    for char in s:
        rows[currRow] += char
        if currRow == 0 or currRow == numRows - 1:
            goingDown = not goingDown
        currRow += 1 if goingDown else -1

    return ''.join(rows)


s = "PAYPALISHIRING"
numRows = 3
print(convert(s,numRows))