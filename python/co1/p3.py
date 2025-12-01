n_list = [12, -1, 3, -2, 4, -3]
pos_list = []
i = 0

while i < len(n_list):
    if n_list[i] > 0:
        pos_list.append(n_list[i])
    i += 1

print("Positive nums is:", pos_list)