def convert(num: str, from_base: int, to_base: int) -> str:
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]


print((convert('12345', 16,  2)))
#1010101001
#0101010110
#681
# """
# 0100 0100 0101 0010
# 0101 1000 0011 0110
# ------------------
# 1001 1100 1000 1000
#      0110
# -------------------
# 1010 0010 1000 1000
# 0110
# -------------------
# 0001 0000 0010 1000 1000
# в 10 будет 10_288

# 0001 0011 1000 0100


# 1000 1000 0010 0110
# 0111 0010 0100 1001
# -------------------
# 0001 0101 1101 1101
# -------------------
# 0001 0101 0111 0111



# """

# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			print(int((y or not y and z)), end=' ')
# 			print(int(x and y and z or x and y and (not z) or x and (not y) and z or (not x) and y and (not z)))



"""

"""





