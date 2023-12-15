from typing import List



def longestCommonPrefix(strs: List[str]) -> str:

    if len(strs) == 1: return strs[0]

    prefix = min(strs)
    for i in range(len(strs)):
        for n in range(len(prefix)+1, -1, -1):

            if prefix[:n] != strs[i][:n]:
                prefix = prefix[:n-1]

        if prefix == "":
            return ""

    return prefix

sp = ["flower","flow","flight"]#["abab","aba","abc"]#["reflower","flow","flight"]#["ab", "a"]#["flower","flow","flight"]
print(longestCommonPrefix(sp))