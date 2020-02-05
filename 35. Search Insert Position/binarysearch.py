def searchInsert(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

nums = [1, 3, 5, 6]
target = 2

print(searchInsert(nums, target)) # 1