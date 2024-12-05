num = int(input("Введите число: "))
result = ""

for i in range(1, num):
    for j in range(2, num):
        if i > num // 2:
            break
        elif num % (i + j) == 0 and i != j:
            result += str(i) + str(j)

print(result)