
def isPalindrome(x: int) -> bool:
    if x< 0: return False

    return str(x)[::-1]==str(x)
