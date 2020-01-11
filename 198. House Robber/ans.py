def rob(nums):        
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]
    if n == 2: return max(nums[0],nums[1])

    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return max(dp[n-1], dp[n-2])

nums = [2,1,1,2]
print(rob(nums)) #4