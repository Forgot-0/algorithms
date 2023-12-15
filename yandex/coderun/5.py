


n = 9
k1 = 0
k2 = 0
spisok_cost = []
sum_cost = 0
index_kypon = []
data = [110, 40, 120, 110, 60]#[35, 40, 101, 59, 63]
for i in range(len(data)):
    cost = data[i]
    sum_cost += cost
    if cost > 100:
        k1 += 1
        index_kypon.append(i)
        cost = 0
    spisok_cost.append(cost)



# print(sum_cost)
# print(k1, k2)
# print(spisok_cost, index_kypon)
