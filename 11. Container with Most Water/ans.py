height = [1,8,6,2,5,4,8,3,7]


def maxArea(height):
    contain = 0
    left, right = 0, len(height)-1
    while left < right:
        leftVal = height[left]
        rightVal = height[right]
        if leftVal > rightVal:
            sum = rightVal*(right-left)
            right -= 1
            if sum > contain:
                contain = sum
        else:
            sum = leftVal*(right-left)
            left += 1
            if sum > contain:
                contain = sum
    return contain

print(maxArea(height))