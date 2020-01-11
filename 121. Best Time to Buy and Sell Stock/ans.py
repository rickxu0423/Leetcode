def maxProfit(prices):        
    n = len(prices)
    ans = 0
    dp = [0 for _ in range(n)]
    Min = float('inf')
    for i in range(n):
        dp[i] = prices[i] - Min
        if dp[i] > ans: ans = dp[i]
        if prices[i] < Min: Min = prices[i]  
    return ans

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(maxProfit(prices1)) #5
print(maxProfit(prices2)) #0