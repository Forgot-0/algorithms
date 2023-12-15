# n = int(input())
# spisok = list(map(int, input().split()))
# sum_s = sum(spisok)
# if sum_s/n*2 != int(sum_s/n*2) or n%2!=0:
#     print(-1)
# else:
#     target = int(sum_s/n*2)
#     left = 0
#     right = len(spisok) - 1
#     while left < right:
#         if spisok[left] + spisok[right] == target:
#             left += 1
#             right -= 1
#         else:
#             print(-1)
#             break

#     else:
#         print(target)


# n, m = map(int, input().split())
# max_l = max(len(str(n-1)), len(str(m-1)))
# count = 0
# for i in range(n):
#     s = str(i).rjust(max_l, '0')
#     if int(s[::-1]) < m:
#         count += 1
# print(count)

# n = 9
# name_t = {}
# answers = []
# quest = [['Ivan', 1], ['Anton', 1], ['Victor', 2], ['Anton', 3], ['Ivan', 5], ['Denis', 10], ['Victor', 11], ['Anton', 11], ['Ivan', 12]]
# s = 0

# for i in range(n):
#     max_exp = 0
#     max_name = 'Z'*10**5
#     name, t = quest[i]
#     t = int(t)

#     if name in name_t:
        
#         if name_t[name][0] != 0:
#             name_t[name][1] += t - name_t[name][0]
#             name_t[name][0] = 0
#         else:
#             name_t[name][0] = t
#             s += name_t[name][1]
#     else:
#         name_t[name] = [t, 0]



#     for key in name_t:
#         if name_t[key][0] != 0:
#             name_t[key][1] += t-name_t[key][0]
#             name_t[key][0] = t 
#             s += name_t[key][1]
            
            
            

#     answers.append([max_name, s-max_exp*2])

# print(answers)



# n = int(input())
# name_t = {}

# for i in range(n):
#     max_exp = 0
#     max_name = 'Z'*10**5
#     s = 0
#     name, t = input().split()
#     t = int(t)

#     if name in name_t:
        
#         if name_t[name][0] != 0:
#             name_t[name][1] += t - name_t[name][0]
#             name_t[name][0] = 0
#         else:
#             name_t[name][0] = t
#     else:
#         name_t[name] = [t, 0]

#     for key in name_t:
#         if name_t[key][0] != 0:
#             name_t[key][1] += t-name_t[key][0]
#             name_t[key][0] = t 
#             s += name_t[key][1]
#             if name_t[key][1] >= max_exp:
#                 max_exp = name_t[key][1]
#                 max_name = min(max_name, key)
#     print(max_name, s-max_exp*2)
