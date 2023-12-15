def longestPalindrome(s:str) -> str:
    max_l = 0
    substr = ''
    for i in range(len(s)):
        for j in range(i+max_l, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                max_l = j-i+1
                substr = s[i:j+1]
    return substr



print(longestPalindrome('a'))