def isLongPressedName(name, typed):
    index1, index2 = 0, 0
    while index1 < len(name):
        if name[index1] != typed[index2]: return False
        while index2 < len(typed)-1 and name[index1] == typed[index2]:
            index2 += 1
            if index1+1<len(name) and name[index1+1] == typed[index2]:
                index1 += 1
        index1 += 1
    return True

name = 'leelee'
typed = 'lleeelee'

print(isLongPressedName(name, typed)) # true