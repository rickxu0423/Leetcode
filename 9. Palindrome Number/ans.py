x = 121


def isPalindrome(x):
    if x < 0 or ( x % 10 == 0 and x != 0):
        return False
    if x < 10:
        return True
    reverse = 0
    while x // 10 >= reverse*10:
        reverse = reverse*10
        reverse += x % 10
        x = x // 10
    if x == reverse or x // 10 == reverse :
        return True
    else: return False

print(isPalindrome(x))