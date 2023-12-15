
def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    
    for i in range(len(s)):
        for n in range(len(s)):
            if len(s[i:n]) == len(set(s[i:n])):
                max_length = max(max_length, len(set(s[i:n])))
            else:
                break

    return max_length

