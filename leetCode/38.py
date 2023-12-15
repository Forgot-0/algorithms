
def countAndSay(n: int) -> str:
    stroka = '1'

    for _ in range(n-1):
        str_l = len(stroka)
        pod_str = ""
        i = 0
        k = 1
        while i < str_l-1:
            if stroka[i] == stroka[i+1]:
                k+=1
                i+=1
            else:
                pod_str += str(k) + stroka[i]
                i+=1
                k = 1
        pod_str += (str(k) + stroka[i])
        stroka = str(pod_str)

    return stroka

n = 6

print(countAndSay(n))




