my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
my_list_len = len(my_list)

while i < my_list_len:
    if my_list[i] == 0:
        i += 1
        continue
    elif my_list[i] < 0:
        break
    else:
        print(my_list[i])
        i += 1
