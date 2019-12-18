nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    n = len(nums)
    SUM = nums[0]
    for i in range(1, n):
        if nums[i-1]>0:
            nums[i] += nums[i-1]    
        SUM = max(nums[i], SUM)
    return SUM
print(maxSubArray(nums))