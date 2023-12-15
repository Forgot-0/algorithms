
def lengthOfLastWord(s: str) -> int:
    spisok = s.split(" ")
    for i in range(len(spisok)-1, -1, -1):
        if spisok[i]: return len(spisok[i])


s = "World"
print(lengthOfLastWord(s))