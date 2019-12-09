nums = [1,3,5,6]
target = 5

def searchInsert(nums, target):
    index = 0
    while index < len(nums):
        if nums[index] == target:
            return index
        if nums[index] > target:
            if index == 0:
                return 0
            return index
        index += 1
    return index

print(searchInsert(nums, target))