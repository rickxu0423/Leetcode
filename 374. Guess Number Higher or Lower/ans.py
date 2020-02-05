def guess(n):
    if n == 6: return 0
    elif n < 6: return 1
    else: return -1

def guessNumber(n):
    start, end = 1, n
    while start <= end:
        mid = (start + end) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            start = mid + 1
        else: end = mid - 1
    return None

print(guessNumber(10)) # 6