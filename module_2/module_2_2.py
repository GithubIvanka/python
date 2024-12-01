first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")

if first == second and second == third and third == first:
    print("3")
elif first == second or second == third or third == first:
    print("2")
else:
    print("0")