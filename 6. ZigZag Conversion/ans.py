s = "PAYPALISHIRING"
numRows = 3

def convert(s, numRows):
    if numRows == 1: return s
    rows = ["" for _ in range(min(numRows,len(s)))]
    curRow = 0
    goingDown = False
    for c in s:
        rows[curRow] += c
        if curRow == 0 or curRow == numRows - 1:
            goingDown = not goingDown
        curRow += 1 if goingDown else -1
    ret = ""
    for row in rows:
        ret += row
    return ret
print(convert(s, numRows))