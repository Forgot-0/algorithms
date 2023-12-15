from typing import List




def shag(ind, a, b):
    if ind == a:
        return [1]
    elif ind == b:
        return [-1]
    return [1, -1]

    

def exist(board: List[List[str]], word: str) -> bool:
    
    for i in range(len(board)):
        
        if not (board[i].count(word[0])):
            continue
        
        j = board[i].index(word[0])
        


print(exist([["A","B","C","E"],["S","F","C","S"],["A","D", "E","E"]], word = "ABCCED"))