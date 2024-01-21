# def convert(num: str, from_base: int, to_base: int) -> str:
# 		num = int(str(num), from_base)
# 		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
# 		answ = alphabet[num%to_base]
# 		while num >= to_base:
# 				num //= to_base
# 				answ += alphabet[num%to_base]
# 		return answ[::-1]


# print((convert('12345', 16,  2)))


# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			print(int((y or not y and z)), end=' ')
# 			print(int(x and y and z or x and y and (not z) or x and (not y) and z or (not x) and y and (not z)))


# min_a = 10**6
# for A1 in range(7, 9):
#     for A2 in range(A1+1, 40):
#         flag = True
#         for x in range(-1_000, 1_000):
#             x *= 0.5
#             D =  7 <= x <= 68
#             C = 29 <= x <= 100
#             A = A1 <= x <= A2
#             if not((D) <= (( (not C) and (not A)) <= (not D))):
#                 flag=False
#                 print(A1, A2, x)
#                 break
#         if flag:
#             min_a = min(A2-A1, min_a)


# def quick_sort(spisok):
#     if len(spisok) <= 1:
#         return spisok

#     midVal = spisok[len(spisok)//2]

#     left = [el for el in spisok if el < midVal]
#     middle = [el for el in spisok if el == midVal]
#     right = [el for el in spisok if el > midVal]

#     return quick_sort(left) + middle + quick_sort(right)


# print(quick_sort([388, 858, 700, 420, 835, 653, 610, 712, 991]))