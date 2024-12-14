def print_params(a=1, b="Строка", c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ["one", False, 7.0]
values_dict = {'a': "two", 'b': True, 'c': 99}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["@", "!"]

print_params(*values_list_2, 42)