nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    dicT = {}
    for i in range(len(nums)):
        if target-nums[i] not in dicT:
            dicT[nums[i]] = i
        else:
            return [dicT[target-nums[i]], i]

print(twoSum(nums, target))