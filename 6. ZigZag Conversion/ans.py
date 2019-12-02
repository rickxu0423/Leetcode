s = "PAYPALISHIRING"
numRows = 3

def convert(s, numRows):
    rows = ["" for _ in range(numRows)]
    index = 0
    rowNumber = 0
    while index < len(s):
        while rowNumber < numRows and index < len(s):
            rows[rowNumber] += s[index]
            rowNumber += 1
            index += 1
        rowNumber = max(0, rowNumber - 2)
        while rowNumber != 0 and index < len(s):
            rows[rowNumber] += s[index]
            rowNumber -= 1
            index += 1
    return "".join(rows)
print(convert(s, numRows))