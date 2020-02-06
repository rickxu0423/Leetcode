def lengthOfLongestSubstring(s):
    if len(s) < 2: return len(s)
    
    left, right = 0, 1
    maxLen = 0
    while right < len(s):
        index = s.find(s[right],left,right)
        if index > -1: left = index + 1
        if right - left + 1 > maxLen: maxLen = right - left + 1
        right += 1
    return maxLen

print(lengthOfLongestSubstring("pwwkew")) #3