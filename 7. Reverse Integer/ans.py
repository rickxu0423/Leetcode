x = -123

def reverse(x):
    rev = 0
    neg = False
    if x < 0:
        x = -x
        neg = True
    while x >= 1:
        pop = x % 10
        x = int(x/10)            
        rev = rev*10 + pop         
        if x >= 1:
            if neg == False and (rev > (2**31-1)/10):
                return 0
            elif neg == True and (-rev < -(2**31)/10):
                return 0
    if neg == False:
        return rev
    else:
        return -rev   

print(reverse(x))