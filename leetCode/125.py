
def isPalindrome(s: str) -> bool:
    a = "qwertyuiopasdfghjklzxcvbnm0123456789"
    stroka = [i.lower() for i in s if i.lower() in a]

    return stroka==stroka[::-1]