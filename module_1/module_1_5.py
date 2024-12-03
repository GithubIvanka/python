immutable_var = (1, "one", 0, "zero")

print(immutable_var)

# immutable_var[0] = 2  <= TypeError: 'tuple' object does not support item assignment
# не получается изменить, так как кортежи являются неизменяемым списком.

mutable_list = ([0, 1, 2, 3],)

mutable_list[0][0] = 99
print(mutable_list)