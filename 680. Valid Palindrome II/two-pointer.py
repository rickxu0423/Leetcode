def validPalindrome(s):
    left, right = 0, len(s) - 1
    counter = 0
    reserve = []
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if counter > 0 and not reserve: 
                return False
            elif counter > 0 and reserve:
                left, right = reserve[0], reserve[1]
                reserve = []
            else:
                reserve = [left, right-1]
                left += 1
                counter += 1
    return True

s = "abcdba"
print(validPalindrome(s)) #true