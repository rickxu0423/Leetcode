s = "abcabcbb"

def lengthOfLongestSubstring(s):
    dicT = {}
    ans = 0
    left, right = 0, 0
    while right < len(s):
        tem = s[right]
        if tem in dicT:
            left = max(dicT[tem], left)
        ans = max(ans, right-left+1)
        dicT[tem] = right + 1
        right += 1
    return ans

print(lengthOfLongestSubstring(s))